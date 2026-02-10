"""Script which runs the Incident Feed ETL pipeline continuously."""

from os import environ as ENV
from dotenv import load_dotenv
from time import sleep

from extract import get_stomp_listener
from transform import get_transformed_message
from load import get_db_connection, upload_data

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
