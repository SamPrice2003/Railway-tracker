"""Script which loads the transformed incident data into the RDS database."""

from os import environ as ENV, _Environ
from time import sleep

from logging import getLogger, basicConfig, INFO
from dotenv import load_dotenv
from psycopg2 import connect, sql
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor, execute_values

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


def upload_service_assignment_data(conn: connection, incident_data: dict) -> None:
    """Uploads the services affected by the incident data as entries in
    the service assignment table. Expects incident_id key in the incident data."""

    logger.info("Uploading service assignment data to RDS database.")

    data = incident_data.copy()

    data["services_affected"] = [(get_service_id(
        conn, service["origin_station"], service["destination_station"]), data["incident_id"]) for service in data["services_affected"]]

    with conn.cursor() as cur:

        execute_values(cur, """
                       INSERT INTO service_assignment (service_id, incident_id)
                       VALUES %s
                       ;
                       """, data["services_affected"])

    logger.info("Finished uploading service assignment data to RDS database.")


def upload_incident_data(conn: connection, incident_data: dict) -> int:
    """Uploads the incident data to the RDS database.
    Returns the incident ID of the incident row created."""

    logger.info("Uploading incident data to RDS database.")

    data = incident_data.copy()

    del data["services_affected"]
    del data["operator"]

    with conn.cursor() as cur:

        cur.execute(sql.SQL(
            """
            INSERT INTO incident ({0})
            VALUES ({1})
            RETURNING incident_id
            ;
            """).format(
                sql.SQL(", ").join(
                    map(lambda col: sql.Identifier(col), incident_data.keys())),
                sql.SQL(", ").join(
                    map(lambda val: sql.Identifier(val), incident_data.values()))
        ))

        incident_id = cur.fetchone()

    conn.commit()

    logger.info("Finished uploading incident data to RDS database.")

    return incident_id


def upload_data(conn: connection, incident_data: dict) -> None:
    """Uploads the incident data to the RDS database and handles uploading
    of any assignment tables too."""

    incident_data["incident_id"] = upload_incident_data(conn, incident_data)

    upload_service_assignment_data(conn, incident_data)


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
