"""Script which loads the transformed incident data into the RDS database."""

from os import environ as ENV, _Environ

from dotenv import load_dotenv


def get_db_connection(config: _Environ):
    """Returns a connection to the Postgres RDS Database"""

    pass


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)
