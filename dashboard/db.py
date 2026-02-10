"""Small helpers for reading and writing to the Postgres database."""

import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DEFAULT_DB_PORT = "5432"
REQUIRED_ENV_KEYS = ("DB_HOST", "DB_NAME", "DB_USERNAME", "DB_PASSWORD")


def get_db_connection():
    """Create a Postgres connection using values from environment variables."""
    missing_keys = [
        key for key in REQUIRED_ENV_KEYS if not os.environ.get(key)]
    if missing_keys:
        missing_text = ", ".join(missing_keys)
        raise KeyError(
            f"Missing environment variables: {missing_text}. "
            "Check your .env file and run Streamlit from the project root."
        )

    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ.get("DB_PORT", DEFAULT_DB_PORT),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )


def fetch_table(sql_query: str, values: tuple | None = None) -> pd.DataFrame:
    """Run a SELECT query and return the results as a DataFrame."""
    connection = get_db_connection()
    try:
        return pd.read_sql(sql_query, connection, params=values)
    finally:
        connection.close()


def run_change(sql_query: str, values: tuple | None = None) -> None:
    """Run an INSERT, UPDATE, or DELETE statement and commit the change."""
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query, values or ())
        connection.commit()
    finally:
        connection.close()


def run_change_returning(sql_query: str, values: tuple | None = None) -> pd.DataFrame:
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


def run_query(sql: str, params: tuple | None = None) -> pd.DataFrame:
    """Backwards compatible name for fetch_table."""
    return fetch_table(sql, values=params)


def run_execute(sql: str, params: tuple | None = None) -> None:
    """Backwards compatible name for run_change."""
    run_change(sql, values=params)


def run_query_returning(sql: str, params: tuple | None = None) -> pd.DataFrame:
    """Backwards compatible name for run_change_returning."""
    return run_change_returning(sql, values=params)
