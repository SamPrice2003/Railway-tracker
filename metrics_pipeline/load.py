"""script to load the services and arrivals data into RDS."""

from os import environ as ENV, _Environ, remove, path
from logging import getLogger, basicConfig, INFO

from transform import transform, get_db_connection
from extract import extract

from psycopg2.extensions import connection
from psycopg2.extras import execute_values

import pandas as pd
from dotenv import load_dotenv


def upload_service_data(data: list[dict], conn: connection) -> None:
    """Uploads the service data to the service table in RDS"""

    sql = f"""
        INSERT INTO service
            (service_uid,
            origin_station_id,
            destination_station_id,
            operator_id
            )
        VALUES %s
        ON CONFLICT (service_uid) DO NOTHING
        """

    with conn.cursor() as cur:
        execute_values(cur, sql, )
        conn.commit()


def upload_arrival_data(data: list[dict], conn: connection) -> None:
    """Uploads the arrival data to the arrival table in RDS"""
    rows = [()]
    sql = f"""
        INSERT INTO arrival
            (scheduled_time,
            actual_time,
            platform_changed,
            arrival_station_id,
            service_id
            )
        VALUES %s
        ON CONFLICT (scheduled_time, actual_time, arrival_station_id, service_id) DO NOTHING
        """

    with conn.cursor() as cur:
        execute_values(cur, sql, rows)
        conn.commit()


def get_service_id_list(conn: connection) -> list[dict]:

    with conn.cursor() as cur:
        cur.execute("SELECT service_id, service_uid FROM service;")

        result = cur.fetchall()

    return result


def get_service_id_dict(service_id_list: list) -> list[dict]:
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

    station_crs_list = ["LBG", "STP", "KGX", "SHF", "LST",
                        "BHM", "MAN", "LDS", "BRI", "EDB"]

    data = extract(ENV, station_crs_list)

    data = transform(ENV, data, conn)

    service_data = data["services"]
    arrivals_data = data["arrivals"]

    print(service_data.dtypes)

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
