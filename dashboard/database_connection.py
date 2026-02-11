"""Small helpers for reading and writing to the Postgres database."""

import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """Create a Postgres connection using values from environment variables."""
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ.get("DB_PORT", 5432),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )


def fetch_dataframe(sql_query: str, values: tuple | None = None) -> pd.DataFrame:
    """Run a SELECT query and return the results as a DataFrame."""
    connection = get_db_connection()
    try:
        return pd.read_sql(sql_query, connection, params=values)
    finally:
        connection.close()


def run_change(sql_query: str, values: tuple) -> None:
    """Run an INSERT, UPDATE, or DELETE statement and commit the change."""
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query, values or ())
        connection.commit()
    finally:
        connection.close()


def run_change_returning(sql_query: str, values: tuple) -> pd.DataFrame:
    """Run a statement with RETURNING and return the returned rows as a DataFrame."""
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query, values or ())
            rows = cursor.fetchall()
            column_names = [col[0] for col in cursor.description]
        connection.commit()
        return pd.DataFrame(rows, columns=column_names)
    finally:
        connection.close()


def load_stations_with_coords() -> pd.DataFrame:
    """Load stations that have valid latitude and longitude values."""
    stations = fetch_dataframe("""
    SELECT
        station_id,
        station_name,
        station_crs,
        latitude,
        longitude
    FROM station
    WHERE latitude IS NOT NULL
      AND longitude IS NOT NULL;
    """)
    if stations is None:
        return pd.DataFrame()
    return stations



