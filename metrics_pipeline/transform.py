"""The transform script which takes extracted data from the RTT API and transforms it, ready to load into RDS."""

from logging import getLogger, basicConfig, INFO
from os import environ as ENV, _Environ

import pandas as pd
from psycopg2 import connect, sql
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

from extract import extract


def convert_data_to_df(data: list) -> pd.DataFrame:
    """Converts a list of dictionaries to a dataframe."""

    return pd.DataFrame(data)


def convert_df_to_csv_for_test(df: pd.DataFrame, filename: str) -> None:
    """GET RID LATER"""

    df.to_csv(f"./test_{filename}.csv")


def get_data_from_csv_for_test(filename: str) -> None:
    """GET RID LATER"""

    df = pd.read_csv(f"./{filename}.csv")

    return df


def get_db_conn(config: _Environ) -> connection:
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
    """Returns a list of dictionaries with station_crs codes along with the station ids and names.
       This is so we can input the arrival data with the valid columns."""

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


def assign_station_id_to_service(df: pd.DataFrame, station_crs_list: list[dict], column_name: str, origin: bool) -> pd.DataFrame:
    """Assigns the operator_station_id based on the station data in the database."""

    station_crs_dict = {}
    for entry in station_crs_list:
        station_name = entry["station_name"].replace(" Rail Station", "")
        station_id = int(entry["station_id"])
        station_crs_dict[station_name] = station_id

    if origin:
        df[column_name] = df["origin_station"].map(station_crs_dict)
    else:
        df[column_name] = df["destination_station"].map(station_crs_dict)

    return df


def assign_operator_id_to_service(df: pd.DataFrame, operator_name_list: list[dict]) -> pd.DataFrame:
    """Assigns the operator name to the operator id in the database."""

    operator_name_dict = {}
    for entry in operator_name_list:
        operator_name = entry["operator_name"]
        operator_id = int(entry["operator_id"])
        operator_name_dict[operator_name] = operator_id

    df["operator_id"] = df["operator_name"].map(operator_name_dict)

    return df

# FORMAT THE DATA NEEDS TO BE IN FOR SERVICES:
# service_id (DONE)
# service_uid (DONE)
# origin_station_id -
# destination_station_id -
# operator_id -


# FORMAT THE DATA NEEDS TO BE IN FOR ARRIVALS:
# arrival id (DONE since generated)
# scheduled_time (DONE)
# actual_time (DONE)
# platform_changed (DONE)
# arrival_station_id -
# service_id -
if __name__ == "__main__":

    load_dotenv()

    station_crs_list = ["LBG", "STP", "KGX", "SHF", "LST"]

    conn = get_db_conn(ENV)

    # data = extract(ENV, station_crs_list=station_crs_list)

    # service_df = convert_data_to_df(data["services"])
    # arrival_df = convert_data_to_df(data["arrivals"])

    service_df = get_data_from_csv_for_test("test_service")
    arrival_df = get_data_from_csv_for_test("test_arrival")

    db_station_ids = get_station_id_list(conn=conn)

    service_df = assign_station_id_to_service(
        service_df, db_station_ids, "origin_station_id", origin=True)

    service_df = assign_station_id_to_service(
        service_df, db_station_ids, "destination_station_id", origin=False)

    db_operator_ids = get_operator_id_list(conn=conn)

    service_df = assign_operator_id_to_service(service_df, db_operator_ids)

    print(service_df[service_df["operator_id"].isna()])
