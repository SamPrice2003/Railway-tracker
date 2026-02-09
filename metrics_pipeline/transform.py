"""The transform script which takes extracted data \
    from the RTT API and transforms it, ready to load into RDS."""

# pylint: disable=unused-argument, redefined-outer-name

from logging import getLogger, basicConfig, INFO
from os import environ as ENV, _Environ

import pandas as pd
from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

from extract import extract

logger = getLogger(__name__)


def get_db_connection(config: _Environ) -> connection:
    """Returns a connection to a PostgreSQL database with the environment variable credentials."""

    return connect(
        dbname=ENV["DB_NAME"],
        host=ENV["DB_HOST"],
        user=ENV["DB_USERNAME"],
        password=ENV["DB_PASSWORD"],
        port=5432,
        cursor_factory=RealDictCursor
    )


def get_station_id_list(conn: connection) -> list[dict]:
    """Returns a list of dictionaries with \
        station_crs codes along with the station ids and names."""

    sql = """SELECT station_id, station_crs, station_name
             FROM station;
             """

    with conn.cursor() as cur:
        cur.execute(sql)

        result = cur.fetchall()

    return result


def get_operator_id_list(conn: connection) -> list[dict]:
    """Returns a list of dictionaries with the operator name and it's ID in the database."""

    sql = """SELECT operator_id, operator_name
             FROM operator;
             """

    with conn.cursor() as cur:
        cur.execute(sql)

        result = cur.fetchall()

    return result


def get_station_name_dict(station_crs_list: list[dict]) -> dict:
    """Gets the station crs dictionary, containing the name and station_id"""

    station_name_dict = {}
    for entry in station_crs_list:
        station_name = entry["station_name"].replace(" Rail Station", "")
        station_id = entry["station_id"]
        station_name_dict[station_name] = station_id

    return station_name_dict


def assign_station_id_to_arrival(df: pd.DataFrame, station_crs_list: list[dict]) -> pd.DataFrame:
    """Assigns the operator_station_id based on the station data in the database."""

    station_crs_dict = {}
    for entry in station_crs_list:
        station_crs = entry["station_crs"]
        station_id = entry["station_id"]
        station_crs_dict[station_crs] = station_id

    df["arrival_station_id"] = df["crs"].map(station_crs_dict).astype("Int64")

    return df


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


def transform(config: _Environ, data: dict, conn: connection) -> dict:
    """Returns a dictionary containing the transformed service and arrival data.
       Apart from service_id in arrival, which needs to be loaded first to access."""

    basicConfig(level=INFO)

    if not data["services"]:
        return {"services": pd.DataFrame(), "arrivals": pd.DataFrame()}

    service_df = pd.DataFrame(data["services"])
    logger.info("Converted services to DataFrame")
    arrival_df = pd.DataFrame(data["arrivals"])
    logger.info("Converted arrivals to DataFrame")

    db_station_ids = get_station_id_list(conn=conn)
    logger.info("Retrieved station ids from RDS")

    station_name_dict = get_station_name_dict(db_station_ids)

    service_df["origin_station_id"] = service_df["origin_station"].map(
        station_name_dict).astype("Int64")
    service_df["destination_station_id"] = service_df["destination_station"].map(
        station_name_dict).astype("Int64")
    logger.info("Assigned service station ids")

    db_operator_ids = get_operator_id_list(conn=conn)
    logger.info("Retrieved operator ids from RDS")

    service_df = assign_operator_id_to_service(service_df, db_operator_ids)
    logger.info("Assigned operator ids to services")

    service_df = service_df[[
        "service_uid", "origin_station_id", "destination_station_id", "operator_id"]]

    arrival_df = assign_station_id_to_arrival(arrival_df, db_station_ids)
    logger.info("Assigned operator ids to arrivals")

    result = {}

    result["services"] = service_df
    result["arrivals"] = arrival_df

    logger.info("Transformation complete")
    return result


if __name__ == "__main__":

    load_dotenv()

    station_crs_list = ["LBG", "STP", "KGX", "SHF", "LST"]

    data = extract(ENV, station_crs_list=station_crs_list)

    conn = get_db_connection(ENV)

    DATA = transform(ENV, data, conn)
