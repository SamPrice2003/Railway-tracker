"""Script which runs the Incident Feed ETL pipeline continuously."""

from os import environ as ENV
from time import sleep

from dotenv import load_dotenv

from incidents_extract import get_stomp_listener
from incidents_transform import get_transformed_message
from load import get_db_connection, upload_data
from alert import get_sns_client, publish_incident

if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    sns_client = get_sns_client(ENV)

    listener = get_stomp_listener(ENV)

    while True:
        message = listener.pop_message()

        if message:
            message = get_transformed_message(message)

            incident_id = upload_data(conn, message)

            publish_incident(ENV, sns_client, conn, incident_id)

        sleep(1)
