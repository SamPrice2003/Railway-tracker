"""Script which cleans and transforms the data to load into the database."""

from os import environ as ENV
from time import sleep

from dotenv import load_dotenv

from extract import get_stomp_listener


def get_filtered_message(message: dict) -> dict:
    """Returns a message with only useful information on incidents for the database.
    This includes summary, operator, start time, end time, url, whether it was planned."""

    filtered_message = {}

    filtered_message["summary"] = message["Summary"]

    filtered_message["operators"] = [op["OperatorName"]
                                     for op in message["Affects"]["Operators"]["AffectedOperator"]]

    filtered_message["incident_start"] = message["ValidityPeriod"]["StartTime"]

    filtered_message["incident_end"] = message["ValidityPeriod"].get("EndTime")

    filtered_message["url"] = message["InfoLinks"]["InfoLink"]["Uri"]

    filtered_message["planned"] = message["Planned"]

    return filtered_message


def get_transformed_message(message: dict) -> dict:
    """Returns the transformed message as a dict with relevant columns for the database.
    Cleans data values and applies formatting."""

    message = get_filtered_message(message)

    return message


if __name__ == "__main__":

    load_dotenv()

    listener = get_stomp_listener(ENV)

    while True:
        message = listener.pop_message()

        if message:
            print(message)

        sleep(1)
