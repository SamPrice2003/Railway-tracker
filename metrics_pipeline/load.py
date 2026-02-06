"""Script to load the services and arrivals data into RDS."""

from os import environ as ENV, _Environ, remove, path
from logging import getLogger, basicConfig, INFO

from transform import transform, get_db_connection
from extract import extract

from psycopg2.extensions import connection

import pandas as pd
from dotenv import load_dotenv

logger = getLogger(__name__)
basicConfig(level=INFO)


def upload_service_data(df: pd.DataFrame, conn: connection) -> None:
    """Uploads the data to the specified table in RDS."""

    df.to_csv("./temp.csv", index=False)

    with conn.cursor() as cur:
        with open("./temp.csv", "r") as f:
            cur.copy_expert("""COPY service
                                    (service_uid,
                                     origin_station_id,
                                     destination_station_id,
                                     operator_id)
                            FROM STDIN
                            WITH CSV HEADER""", f)

        conn.commit()

    if path.exists("./temp.csv"):
        remove("./temp.csv")

    logger.info("Uploaded service data.")


def upload_arrival_data(df: pd.DataFrame, conn: connection) -> None:
    """Uploads the data to the specified table in RDS."""

    df.to_csv("./temp.csv", index=False)

    with conn.cursor() as cur:
        with open("./temp.csv", "r") as f:
            cur.copy_expert("""COPY arrival
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

    logger.info("Uploaded arrival data.")


def get_service_id_list(conn: connection) -> list[dict]:

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


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    station_crs_list = ["LST"]

    data = extract(ENV, station_crs_list)

    transformed_data = transform(data, conn)

    service_data = transformed_data["services"]
    arrivals_data = transformed_data["arrivals"]

    upload_service_data(service_data, conn)

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

    upload_arrival_data(arrivals_data, conn)
