"""Script to load the services and arrivals data into RDS."""

# pylint: disable=unused-argument, redefined-outer-name
from logging import getLogger, basicConfig, INFO
from os import environ as ENV, _Environ, remove, path

from dotenv import load_dotenv
import pandas as pd
from psycopg2.extensions import connection
from extract import extract
from transform import transform, get_db_connection


logger = getLogger(__name__)
basicConfig(level=INFO)


def create_service_staging_table(conn: connection) -> None:
    """Creates a temporary staging table for the new service data."""

    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS service_staging (
                    service_uid VARCHAR(6),
                    origin_station_id INT,
                    destination_station_id INT,
                    operator_id INT);
                    """)
    logger.info("Created service staging table")


def create_arrival_staging_table(conn: connection) -> None:
    """Creates a temporary staging table for the new arrival data."""

    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS arrival_staging (
                    scheduled_time TIMESTAMP,
                    actual_time TIMESTAMP,
                    platform_changed BOOLEAN,
                    arrival_station_id INT,
                    service_id INT);
                    """)

    logger.info("Created arrival staging table")


def upload_service_staging_data(df: pd.DataFrame, conn: connection) -> None:
    """Uploads the data to the staging service table in RDS."""

    df.to_csv("./temp.csv", index=False)

    with conn.cursor() as cur:
        with open("./temp.csv", "r", encoding="utf-8") as f:
            cur.copy_expert("""COPY service_staging
                                    (service_uid,
                                     origin_station_id,
                                     destination_station_id,
                                     operator_id)
                            FROM STDIN
                            WITH CSV HEADER""", f)

        conn.commit()

    if path.exists("./temp.csv"):
        remove("./temp.csv")

    logger.info("Uploaded service staging data.")


def upload_arrival_staging_data(df: pd.DataFrame, conn: connection) -> None:
    """Uploads the arrival data to the staging arrival table in RDS."""

    df.to_csv("./temp.csv", index=False)

    with conn.cursor() as cur:
        with open("./temp.csv", "r", encoding="utf-8") as f:
            cur.copy_expert("""COPY arrival_staging
                                    (scheduled_time,
                                     actual_time,
                                     platform_changed,
                                     arrival_station_id,
                                     service_id)
                            FROM STDIN
                            WITH CSV HEADER""", f)

        conn.commit()

    if path.exists("./temp.csv"):
        remove("./temp.csv")

    logger.info("Uploaded arrival staging data.")


def merge_service_tables(conn: connection) -> None:
    """Merges the service staging table with the service table."""

    with conn.cursor() as cur:
        cur.execute("""
                    MERGE INTO service AS S
                    USING service_staging AS SS
                    ON S.service_uid = SS.service_uid
                    WHEN MATCHED AND (
                    S.origin_station_id IS DISTINCT FROM SS.origin_station_id
                    OR
                    S.destination_station_ID IS DISTINCT FROM SS.destination_station_id
                    OR
                    S.operator_id IS DISTINCT FROM SS.operator_id)
                    THEN
                        UPDATE SET
                            origin_station_id = SS.origin_station_id,
                            destination_station_id = SS.destination_station_id,
                            operator_id = SS.operator_id
                    WHEN NOT MATCHED THEN
                        INSERT (service_uid,
                                origin_station_id,
                                destination_station_id,
                                operator_id)
                        VALUES (SS.service_uid,
                                SS.origin_station_id,
                                SS.destination_station_id,
                                SS.operator_id);
                    """)
        conn.commit()

    logger.info("Merged service data")


def merge_arrival_tables(conn: connection) -> None:
    """Merges the arrival staging table with the arrival table."""

    with conn.cursor() as cur:
        cur.execute("""
                    MERGE INTO arrival AS A
                    USING arrival_staging AS S
                    ON A.scheduled_time = S.scheduled_time
                    AND A.arrival_station_id = S.arrival_station_id
                    AND A.service_id = S.service_id
                    WHEN MATCHED AND (
                        A.actual_time IS DISTINCT FROM S.actual_time
                        OR
                        A.platform_changed IS DISTINCT FROM S.platform_changed)
                    THEN 
                        UPDATE SET
                            actual_time = S.actual_time,
                            platform_changed = S.platform_changed
                    WHEN NOT MATCHED THEN
                        INSERT (scheduled_time,
                                actual_time,
                                platform_changed,
                                arrival_station_id,
                                service_id)
                        VALUES (S.scheduled_time,
                                S.actual_time,
                                S.platform_changed,
                                S.arrival_station_id,
                                S.service_id);
                    """)
        conn.commit()

    logger.info("Merged arrival data")


def remove_staging_table(conn: connection, table_name: str) -> None:
    """Removes a staging table in the database to declutter."""

    if table_name not in ["service", "arrival"]:
        raise ValueError(f"{table_name} table does not exist.")

    with conn.cursor() as cur:
        cur.execute(f"""
                    DROP TABLE IF EXISTS {table_name}_staging;
                    """)
    logger.info(f"Removed {table_name}_staging table")


def get_service_id_list(conn: connection) -> list[dict]:
    """Retrieves the list of service ids for assignment to arrivals."""
    with conn.cursor() as cur:
        cur.execute("SELECT service_id, service_uid FROM service;")

        result = cur.fetchall()

    return result


def get_service_id_dict(service_id_list: list) -> pd.DataFrame:
    """Assigns a service id to each arrival so we can upload properly."""

    service_id_dict = {}

    for entry in service_id_list:
        service_id = entry["service_id"]
        service_uid = entry["service_uid"]
        service_id_dict[service_uid] = service_id

    return service_id_dict


def load(config: _Environ, conn: connection, data: dict) -> None:
    """Loads the API data into the database."""

    transformed_data = transform(ENV, data, conn)

    service_data = transformed_data["services"]
    arrivals_data = transformed_data["arrivals"]

    create_service_staging_table(conn)
    upload_service_staging_data(service_data, conn)
    merge_service_tables(conn)
    remove_staging_table(conn, "service")

    service_id_list = get_service_id_list(conn)
    service_id_dict = get_service_id_dict(service_id_list)

    arrivals_data["service_id"] = arrivals_data["service_uid"].map(
        service_id_dict).astype("Int64")
    arrivals_data = arrivals_data[[
        "scheduled_arr_time",
        "actual_arr_time",
        "platform_changed",
        "arrival_station_id",
        "service_id"]]

    create_arrival_staging_table(conn)
    upload_arrival_staging_data(arrivals_data, conn)
    merge_arrival_tables(conn)
    remove_staging_table(conn, "arrival")

    logger.info("Completed pipeline")


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    station_crs_list = ["LBG", "STP", "KGX", "SHF", "LST"]

    data = extract(ENV, station_crs_list)

    load(ENV, conn, data)
