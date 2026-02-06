"""The transform script which takes extracted data from the RTT API and transforms it, ready to load into RDS."""

from logging import getLogger, basicConfig, INFO
from os import environ as ENV, _Environ

import pandas as pd
from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

from extract import extract

logger = getLogger(__name__)
basicConfig(level=INFO)


def get_db_connection(config: _Environ) -> connection:
    """Returns a connection to a PostgreSQL database with the environment variable credentials."""

    return connect(
        dbname=config["DB_NAME"],
        host=config["DB_HOST"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        port=5432,
        cursor_factory=RealDictCursor
    )


def get_station_id_list(conn: connection) -> list[dict]:
    """Returns a list of dictionaries with station_crs codes
    along with the station ids and names."""

    sql = """SELECT station_id, station_crs, station_name
             FROM station;
             """

    with conn.cursor() as cur:
        cur.execute(sql)

        result = cur.fetchall()

    logger.info("Retrieved station ids from RDS.")

    return result


def get_operator_id_list(conn: connection) -> list[dict]:
    """Returns a list of dictionaries with the operator name and its ID in the database."""

    sql = """SELECT operator_id, operator_name
             FROM operator;
             """

    with conn.cursor() as cur:
        cur.execute(sql)

        result = cur.fetchall()

    logger.info("Retrieved operator ids from RDS")

    return result


def get_station_dict(station_crs_list: list[dict]) -> dict:
    """Returns a station dict from list of dicts which maps
    station names to their ids"""

    station_name_dict = {}
    for entry in station_crs_list:
        station_name = entry["station_name"].replace(" Rail Station", "")
        station_name_dict[station_name] = entry["station_id"]

    return station_name_dict


def assign_station_id_to_arrival(arrival_df: pd.DataFrame, station_crs_list: list[dict]) -> pd.DataFrame:
    """Assigns the arrival_station_id based on the station data in the database."""

    station_crs_dict = {}
    for entry in station_crs_list:
        station_crs = entry["station_crs"]
        station_id = entry["station_id"]
        station_crs_dict[station_crs] = station_id

    arrival_df["arrival_station_id"] = arrival_df["crs"].map(
        station_crs_dict).astype("Int64")

    return arrival_df


def assign_operator_id_to_service(df: pd.DataFrame, operator_name_list: list[dict]) -> pd.DataFrame:
    """Assigns the operator name to the operator id in the database."""

    operator_name_dict = {}
    for entry in operator_name_list:
        operator_name = entry["operator_name"]
        operator_id = entry["operator_id"]
        operator_name_dict[operator_name] = operator_id

    df["operator_id"] = df["operator_name"].map(
        operator_name_dict).astype("Int64")

    return df


def drop_existing_services(conn: connection, services_df: pd.DataFrame) -> pd.DataFrame:
    """Returns a dataframe which has deleted all services already existing in the service table."""

    sql = """SELECT service_uid
            FROM service
            ;"""

    with conn.cursor() as cur:
        cur.execute(sql)

        existing_services = [service_dict["service_uid"]
                             for service_dict in cur.fetchall()]

    return services_df[~services_df["service_uid"].isin(existing_services)]


def get_existing_arrivals(conn: connection) -> pd.DataFrame:
    """Returns a dataframe of the existing arrivals in the arrivals table."""

    sql = """SELECT 
                scheduled_time AS scheduled_arr_time,
                actual_time AS actual_arr_time,
                platform_changed,
                arrival_station_id,
                service_uid
            FROM arrival
            JOIN service
                USING (service_id)
            ORDER BY service_uid, actual_time
            ;"""

    with conn.cursor() as cur:
        cur.execute(sql)

        return pd.DataFrame(cur.fetchall())


def get_not_existing_arrivals(conn: connection, arrivals_df: pd.DataFrame) -> pd.DataFrame:
    """Returns a dataframe which contains arrivals not existing in the arrival table
    regardless of the actual_arr_time column."""

    existing_arrivals_df = get_existing_arrivals(conn)

    if existing_arrivals_df.empty:
        return arrivals_df

    df = arrivals_df.merge(existing_arrivals_df, on=[
                           "scheduled_arr_time", "arrival_station_id", "service_uid"], how='left', indicator=True)

    df = df[df['_merge'] == 'left_only'].drop(columns='_merge')

    df = df.rename(columns={"actual_arr_time_x": "actual_arr_time",
                            "platform_changed_x": "platform_changed"})

    return df


def get_updating_arrivals(conn: connection, arrivals_df: pd.DataFrame) -> pd.DataFrame:
    """Returns the arrivals that will update an existing row in the arrivals table by actual_arr_time."""

    existing_arrivals_df = get_existing_arrivals(conn)

    pass

    # if existing_arrivals_df.empty:
    #     return pd.DataFrame()

    # return arrivals_df.merge(existing_arrivals_df, on=[
    #     "scheduled_arr_time", "arrival_station_id", "service_uid"], how='inner')


def transform(data: dict, conn: connection) -> dict:
    """Returns a dictionary containing the transformed service and arrival data.
       Apart from service_id in arrival, which needs to be loaded first to access."""

    service_df = pd.DataFrame(data["services"])
    arrival_df = pd.DataFrame(data["arrivals"])

    db_station_ids = get_station_id_list(conn=conn)

    station_dict = get_station_dict(db_station_ids)

    service_df["origin_station_id"] = service_df["origin_station"].map(
        station_dict).astype("Int64")
    service_df["destination_station_id"] = service_df["destination_station"].map(
        station_dict).astype("Int64")

    db_operator_ids = get_operator_id_list(conn=conn)

    service_df = assign_operator_id_to_service(service_df, db_operator_ids)[["service_uid", "origin_station_id",
                                                                             "destination_station_id", "operator_id"]]

    arrival_df = assign_station_id_to_arrival(arrival_df, db_station_ids)[["scheduled_arr_time",
                                                                           "actual_arr_time", "platform_changed",
                                                                           "arrival_station_id", "service_uid"]]

    result = {
        "services": drop_existing_services(conn, service_df),
        "arrivals": get_not_existing_arrivals(conn, arrival_df),
        "updating_arrivals": get_updating_arrivals(conn, arrival_df)
    }

    print(result["updating_arrivals"])

    logger.info("Transformed all data.")

    return result


if __name__ == "__main__":

    load_dotenv()

    station_crs_list = ["LBG", "STP", "KGX", "SHF", "LST",]

    data = extract(ENV, station_crs_list=station_crs_list)

    conn = get_db_connection(ENV)

    transformed_data = transform(data, conn)

    print(transformed_data)
