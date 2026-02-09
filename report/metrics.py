"""Script to generate railway metrics for today."""

from os import environ as ENV, _Environ
from logging import getLogger, basicConfig, INFO

from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv


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


def get_query_result(conn: connection, query: str) -> int | None:
    """Returns the result of a query on the database."""

    with conn.cursor() as cur:
        cur.execute(query)

        return cur.fetchone()


def get_query_results(conn: connection, query: str) -> int | None:
    """Returns the results of a query on the database."""

    with conn.cursor() as cur:
        cur.execute(query)

        return cur.fetchall()


def get_average_delay(conn: connection) -> int:
    """Returns the average delay over all trains that are on time or delayed in minutes."""

    query = """
            SELECT AVG(EXTRACT(MINUTE FROM (actual_time - scheduled_time))) AS average_delay_mins
            FROM arrival
            WHERE arrival_date = CURRENT_DATE AND actual_time >= scheduled_time
            ;
            """

    return get_query_result(conn, query).get("average_delay_mins")


def get_total_cancelled_services(conn: connection) -> int:
    """Returns the total number of cancelled services."""

    query = """
            SELECT COUNT(*) AS cancelled_count
            FROM (
                SELECT COUNT(*) AS cancelled_counts
                FROM arrival
                WHERE arrival_date = CURRENT_DATE AND location_cancelled = TRUE
                GROUP BY service_id
                )
            WHERE cancelled_counts > 0
            ;
            """

    return get_query_result(conn, query).get("cancelled_count")


def get_total_services(conn: connection) -> int:
    """Returns the total number of services that ran today."""

    query = """
            SELECT COUNT(DISTINCT service_id)
            FROM arrival
            WHERE arrival_date = CURRENT_DATE
            ;
            """

    return get_query_result(conn, query).get("count")


def get_total_delayed_services(conn: connection) -> int:
    """Returns the total number of delays that were delayed by at least 1 minute."""

    query = """
            SELECT COUNT(DISTINCT service_id)
            FROM arrival
            WHERE arrival_date = CURRENT_DATE AND actual_time >= scheduled_time + INTERVAL '1 minute' 
            """

    return get_query_result(conn, query).get("count")


def get_total_delayed_arrivals(conn: connection, delay_mins: int, max_delay: int = None) -> int:
    """Returns the total number of arrivals that were delayed by at least delay_mins minutes."""

    query = """
            SELECT COUNT(*)
            FROM arrival
            WHERE arrival_date = CURRENT_DATE AND actual_time >= scheduled_time + INTERVAL '{} minute' 
            """.format(delay_mins)

    if max_delay:
        query += """AND actual_time <= scheduled_time + INTERVAL '{} minute'""".format(
            max_delay)

    return get_query_result(conn, query).get("count")


def get_total_delayed_services_between_times(conn: connection, start_time: str, end_time: str) -> int:
    """Returns the total number of delayed services between two times of day.
    The parameters must be strings of time e.g. '16:30' and '21:30'."""

    query = """
            SELECT COUNT(*)
            FROM arrival
            WHERE arrival_date = CURRENT_DATE AND actual_time >= '{}' AND actual_time <= '{}' AND actual_time >= scheduled_time + INTERVAL '1 minute'
            ;
            """.format(start_time, end_time)

    return get_query_result(conn, query).get("count")


def get_most_delayed_service(conn: connection) -> dict:
    """Returns the details of the most delayed service arrival."""

    query = """
            SELECT
                scheduled_time,
                actual_time,
                ARR.station_name AS arrival_station_name,
                OS.station_name AS origin_station_name,
                DS.station_name AS destination_station_name,
                EXTRACT(MINUTE FROM (actual_time - scheduled_time)) AS delay_mins
            FROM arrival A
            JOIN service S
                USING (service_id)
            JOIN station ARR
                ON (A.arrival_station_id = ARR.station_id)
            JOIN station OS
                ON (S.origin_station_id = OS.station_id)
            JOIN station DS
                ON (S.destination_station_id = DS.station_id)
            WHERE arrival_date = CURRENT_DATE AND scheduled_time IS NOT NULL AND actual_time IS NOT NULL
            ORDER BY EXTRACT(MINUTE FROM (actual_time - scheduled_time)) DESC
            LIMIT 1
            ;
            """

    return get_query_result(conn, query)


def get_most_delayed_lines(conn: connection, limit: int = 5) -> list[dict]:
    """Returns a list of the most delayed lines and their minutes delayed."""

    query = """
            SELECT
            	operator_name,
            	SUM(EXTRACT(MINUTE FROM (actual_time - scheduled_time))) AS total_delay_mins
            FROM arrival
            JOIN service
            	USING (service_id)
            JOIN operator
            	USING (operator_id)
            WHERE arrival_date = CURRENT_DATE AND actual_time >= scheduled_time
            GROUP BY operator_id, operator_name
            ORDER BY SUM(EXTRACT(MINUTE FROM (actual_time - scheduled_time))) DESC
            LIMIT {}
            ;
            """.format(limit)

    return get_query_results(conn, query)


def get_most_delayed_stations(conn: connection, limit: int = 5) -> list[dict]:
    """Returns a list of the most delayed stations with the number of services delayed."""

    query = """
            SELECT
            	station_name,
            	SUM(EXTRACT(MINUTE FROM (actual_time - scheduled_time))) AS total_delay_mins
            FROM arrival A
            JOIN station S
            	ON (A.arrival_station_id = S.station_id)
            WHERE arrival_date = CURRENT_DATE AND actual_time >= scheduled_time
            GROUP BY station_id, station_name
            ORDER BY SUM(EXTRACT(MINUTE FROM (actual_time - scheduled_time))) DESC
            LIMIT {}
            ;
            """.format(limit)

    return get_query_results(conn, query)


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    print(get_most_delayed_stations(conn))
