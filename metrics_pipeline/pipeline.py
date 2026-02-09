"""The combined pipeline script for the docker image."""


from logging import getLogger, basicConfig, INFO
from os import environ as ENV, _Environ, remove, path
import json
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

from dotenv import load_dotenv
import pandas as pd

from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor

from extract import extract
from transform import transform, get_db_connection
from load import load


logger = getLogger()
logger.setLevel(INFO)


def handler(event=None, context=None):
    """Executes the pipeline, in the valid format for a lambda function."""

    logger.info("Pipeline started")

    conn = get_db_connection(ENV)

    chosen_stations = ["LBG", "STP", "KGX", "SHF", "LST"]
    extracted_data = extract(ENV, chosen_stations)
    print(extracted_data["services"])
    transformed_data = transform(ENV, extracted_data, conn)

    load(ENV, conn, transformed_data)


if __name__ == "__main__":

    load_dotenv()

    handler()
