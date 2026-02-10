"""Script which cleans and transforms the data to load into the database."""

# pylint: disable=redefined-outer-name,line-too-long

from os import environ as ENV
from time import sleep
from datetime import datetime
from re import sub, split
from logging import getLogger, basicConfig, INFO

from dotenv import load_dotenv

from extract import get_stomp_listener

logger = getLogger(__name__)
basicConfig(level=INFO)


def get_services_affected(services_str: str) -> list[dict]:
    """Returns the services affected by the incident, each dict comprises
    of an origin station key and destination station key for the service."""

    services_str = sub(r"^<p>", "", services_str)
    services_str = sub(r"<\/p>$", "", services_str)

    services_lst = split(r"<\/p><p>|,", services_str)

    services_lst = [sub(r".*[bB]etween ", "", service)
                    for service in services_lst]

    services_lst = [sub(r" \/ .+ and|and .+ / |and", ",", service)
                    for service in services_lst]

    services_lst = [service.split(",") for service in services_lst]

    services_lst = [{"origin_station": service[0].strip(),
                     "destination_station": service[-1].strip()} for service in services_lst]

    return services_lst


def get_corrected_types(message: dict) -> dict:
    """Returns a dict which corrects the types of some values in the message."""

    typed_message = message.copy()

    typed_message["incident_start"] = datetime.fromisoformat(
        message["incident_start"])

    if message.get("incident_end"):
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
    This includes summary, operator, start time, end time, url, whether it was planned, services affected."""

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

    filtered_message["services_affected"] = get_services_affected(
        message["Affects"]["RoutesAffected"])

    return filtered_message


def get_transformed_message(message: dict) -> dict:
    """Returns the transformed message as a dict with relevant columns for the database.
    Cleans data values and applies formatting."""

    logger.info("Started transformation of incident data.")

    filtered_message = get_filtered_message(message.copy())

    transformed_message = get_corrected_types(filtered_message)

    logger.info("Finished transformation of incident data.")

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
