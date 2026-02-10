"""The combined pipeline script for the docker image."""

# pylint: disable=unused-argument

from logging import getLogger, INFO
from os import environ as ENV

from dotenv import load_dotenv

from extract import extract
from transform import transform, get_db_connection
from load import load


logger = getLogger()
logger.setLevel(INFO)


def handler(event=None, context=None):
    """Executes the pipeline, in the valid format for a lambda function."""

    logger.info("Pipeline started")

    conn = get_db_connection(ENV)

    chosen_stations = ["LBG", "STP", "KGX", "SHF", "LST", "WFJ"]
    extracted_data = extract(ENV, chosen_stations)
    transformed_data = transform(ENV, extracted_data, conn)

    load(ENV, conn, transformed_data)


if __name__ == "__main__":

    load_dotenv()

    handler()
