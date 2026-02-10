"""Script for sending an alert via SNS to subscribed users about incidents."""

from os import environ as ENV, _Environ
from time import sleep
from datetime import datetime

from dotenv import load_dotenv
from boto3 import client
from psycopg2.extensions import connection

from extract import get_stomp_listener
from transform import get_transformed_message
from load import get_db_connection, upload_data


def get_sns_client(config: _Environ) -> client:
    """Returns an AWS SNS client."""

    return client(
        "sns",
        aws_access_key_id=config["AWS_ACCESS_KEY"],
        aws_secret_access_key=config["AWS_SECRET_KEY"]
    )


def get_sns_topic_arn(sns_client: client, topic_name: str) -> str:
    """Returns an SNS topic ARN. Returns the ARN if it already exists.
    Creates a new SNS topic and returns the ARN if it does not already exist."""

    response = sns_client.create_topic(
        Name=topic_name
    )

    return response["TopicArn"]


def get_stations_affected(conn: connection, incident_id: int) -> list[str]:
    """Returns the stations affected by an incident given its id."""

    with conn.cursor() as cur:
        cur.execute("""
                    SELECT DISTINCT station_name
                    FROM incident
                    JOIN service_assignment
                        USING (incident_id)
                    JOIN service
                        USING (service_id)
                    JOIN arrival
                        ON (service.service_id = arrival.service_id)
                    JOIN station
                        ON (arrival.arrival_station_id = station.station_id)
                    WHERE arrival_date >= CURRENT_DATE AND incident_id = {}
                    ;
                    """.format(incident_id))

        return [row["station_name"] for row in cur.fetchall()]


def get_incident_service_details(conn: connection, incident_id: int) -> list[dict]:
    """Returns further details about the incident outside of its table such as
    service, operator, origin and destination stations."""

    with conn.cursor() as cur:
        cur.execute("""
                    SELECT
                        operator_name,
                        OS.station_name AS origin_station_name,
                        DS.station_name AS destination_station_name
                    FROM incident
                    JOIN service_assignment
                        USING (incident_id)
                    JOIN service
                        USING (service_id)
                    JOIN operator
                        USING (operator_id)
                    JOIN station OS
                        ON (service.origin_station_id = OS.station_id)
                    JOIN station DS
                        ON (service.destination_station_id  = DS.station_id)
                    WHERE incident_id = {}
                    ;
                    """.format(incident_id))

        return cur.fetchall()


def generate_email(conn: connection, incident_id: int) -> dict:
    """Returns an email subject and message in a dict, using information
    on the database found via the incident_id."""

    subject = "ALERT: National Rail Incident Detection"

    with conn.cursor() as cur:
        cur.execute("""
                    SELECT *
                    FROM incident
                    WHERE incident_id = {}
                    """.format(incident_id))

        incident_details = cur.fetchone()

    service_details = get_incident_service_details(conn, incident_id)

    if incident_details.get("incident_end"):
        incident_end = datetime.strftime(
            incident_details.get("incident_end"), "%d/%m/%Y %H:%M:%S")
        incident_timing = f"is expected to last from {datetime.strftime(incident_details["incident_start"], '%d/%m/%Y %H:%M:%S')} to {incident_end}"
    else:
        incident_timing = f"occurred at {datetime.strftime(incident_details["incident_start"], '%d/%m/%Y %H:%M:%S')}"

    message_start = f"""We recently detected an incident affecting a station you are subscribed to.

{incident_details.get("summary", "National Rail has not provided much information on this incident")}.

This incident {incident_timing}.
"""

    message_end = f"""
This was{"" if incident_details["planned"] else " not"} planned by National Rail in advance.

More information on the incident can be found at this link: {incident_details["url"]}.

Kind regards,

Signal Shift Team"""

    if len(service_details) == 0:
        message = message_start + message_end
    else:
        message = message_start + f"""
Services affected include:
- {"\n- ".join([f"{detail["origin_station_name"]} and {detail["destination_station_name"]} ({detail["operator_name"]})" for detail in service_details])}
""" + message_end

    return {
        "subject": subject,
        "message": message
    }


def publish_incident(config: _Environ, sns_client: client, conn: connection, incident_id: int) -> None:
    """Publishes an incident to the SNS topic via the config."""

    sns_topic_arn = get_sns_topic_arn(sns_client, config["SNS_TOPIC"])

    stations = get_stations_affected(conn, incident_id)

    email = generate_email(conn, incident_id)

    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=email["message"],
        Subject=email["subject"],
        MessageAttributes={
            "stations": {
                "DataType": "String.Array",
                "StringValue": f"{stations}"
            }
        }
    )


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
