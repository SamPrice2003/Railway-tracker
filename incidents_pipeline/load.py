"""Script which loads the transformed incident data into the RDS database."""

from os import environ as ENV, _Environ
from time import sleep

from dotenv import load_dotenv
from psycopg2 import connect, sql
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor

from extract import get_stomp_listener
from transform import get_transformed_message


def get_db_connection(config: _Environ) -> connection:
    """Returns a connection to the Postgres RDS Database"""

    return connect(
        host=config["DB_HOST"],
        dbname=config["DB_NAME"],
        port=config["DB_PORT"],
        user=config["DB_USERNAME"],
        password=config["DB_PASSWORD"],
        cursor_factory=RealDictCursor
    )


def get_service_id(conn: connection, origin_station: str, destination_station: str, operator_name: str) -> int:
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
            WHERE OS.station_name = '{0}' AND DS.station_name = '{1}' AND O.operator_name = '{2}'
            ;
            """).format(
            sql.Literal(origin_station),
            sql.Literal(destination_station),
            sql.Literal(operator_name)
        ))

        return cur.fetchone()


def upload_data(conn: connection, incident_data: dict) -> None:
    """Uploads the incident_data to the RDS database."""

    with conn.cursor() as cur:
        pass


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    listener = get_stomp_listener(ENV)

    while True:
        message = listener.pop_message()

        if message:
            message = get_transformed_message(message)
            print(message)

        sleep(1)
