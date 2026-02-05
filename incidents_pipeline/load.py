"""Script which loads the transformed incident data into the RDS database."""

from os import environ as ENV, _Environ
from time import sleep

from logging import getLogger, basicConfig, INFO
from dotenv import load_dotenv
from psycopg2 import connect, sql
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor

from extract import get_stomp_listener
from transform import get_transformed_message

logger = getLogger(__name__)
basicConfig(level=INFO)


def get_db_connection(config: _Environ) -> connection:
    """Returns a connection to the Postgres RDS Database"""

    conn = connect(
        host=config["DB_HOST"],
        dbname=config["DB_NAME"],
        port=config["DB_PORT"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        cursor_factory=RealDictCursor
    )

    logger.info("Established connection to RDS database.")

    return conn


def get_service_id(conn: connection, origin_station: str, destination_station: str) -> int:
    """Returns the service_id of the service the incident data refers to."""

    with conn.cursor() as cur:
        cur.execute(sql.SQL("""
            SELECT S.service_id
            FROM service S
            JOIN station OS
                ON S.origin_station_id = OS.station_id
            JOIN station DS
                ON S.destination_station_id = OS.station_id
            JOIN operator O
                ON S.operator_id = O.operator_id
            WHERE OS.station_name = '{0}' AND DS.station_name = '{1}'
            ;
            """).format(
            sql.Literal(origin_station),
            sql.Literal(destination_station)
        ))

        return cur.fetchone()


def upload_data(conn: connection, incident_data: dict) -> None:
    """Uploads the incident data to the RDS database."""

    logger.info("Uploading incident data to RDS database.")

    data = incident_data.copy()

    origin_station = data["services_affected"][0]["origin_station"]
    destination_station = data["services_affected"][0]["destination_station"]

    del data["services_affected"]
    del data["operator"]

    with conn.cursor() as cur:

        data["service_id"] = get_service_id(
            conn, origin_station, destination_station)

        cur.execute(sql.SQL(
            """
            INSERT INTO incident ({0})
            VALUES ({1})
            ;
            """).format(
                sql.SQL(", ").join(
                    map(lambda col: sql.Identifier(col), incident_data.keys())),
                sql.SQL(", ").join(
                    map(lambda val: sql.Identifier(val), incident_data.values()))
        ))

    conn.commit()

    logger.info("Finished uploading incident data to RDS database.")


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    listener = get_stomp_listener(ENV)

    while True:
        message = listener.pop_message()

        if message:
            message = get_transformed_message(message)
            upload_data(conn, message)

        sleep(1)
