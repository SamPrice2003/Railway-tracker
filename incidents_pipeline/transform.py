"""Script which cleans and transforms the data to load into the database."""

from os import environ as ENV
from time import sleep
from datetime import datetime

from dotenv import load_dotenv

from extract import get_stomp_listener


def get_corrected_types(message: dict) -> dict:
    """Returns a dict which corrects the types of some values in the message."""

    typed_message = message.copy()

    typed_message["incident_start"] = datetime.fromisoformat(
        message["incident_start"])

    typed_message["incident_end"] = datetime.fromisoformat(
        message["incident_end"])

    if message["planned"].lower() == "true":
        typed_message["planned"] = True
    elif message["planned"].lower() == "false":
        typed_message["planned"] = False
    else:
        typed_message["planned"] = None

    return typed_message


def get_filtered_message(message: dict) -> dict:
    """Returns a message with only useful information on incidents for the database.
    This includes summary, operator, start time, end time, url, whether it was planned."""

    filtered_message = {}

    filtered_message["summary"] = message["Summary"]

    if isinstance(message["Affects"]["Operators"]["AffectedOperator"], list):
        filtered_message["operators"] = [op["OperatorName"]
                                         for op in message["Affects"]["Operators"]["AffectedOperator"]]
    else:
        filtered_message["operators"] = [message["Affects"]
                                         ["Operators"]["AffectedOperator"]["OperatorName"]]

    filtered_message["incident_start"] = message["ValidityPeriod"]["StartTime"]

    filtered_message["incident_end"] = message["ValidityPeriod"].get("EndTime")

    filtered_message["url"] = message["InfoLinks"]["InfoLink"]["Uri"]

    filtered_message["planned"] = message["Planned"]

    return filtered_message


def get_transformed_message(message: dict) -> dict:
    """Returns the transformed message as a dict with relevant columns for the database.
    Cleans data values and applies formatting."""

    filtered_message = get_filtered_message(message.copy())

    transformed_message = get_corrected_types(filtered_message)

    return transformed_message


if __name__ == "__main__":

    load_dotenv()

    listener = get_stomp_listener(ENV)

    while True:
        message = listener.pop_message()

        if message:
            message = get_transformed_message(message)
            print(message)

        sleep(1)
