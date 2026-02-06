""" The extract script responsible for extracting static data from the RTT api """

from os import environ as ENV, _Environ
import json
from logging import getLogger, basicConfig, INFO
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


logger = getLogger(__name__)


def get_basic_auth(config: _Environ):
    """Returns a basic auth from credentials."""

    basic = HTTPBasicAuth(
        username=ENV["RTT_USER"], password=ENV["RTT_PASSWORD"])

    return basic


def get_crs(station_name: str) -> str:
    """Returns the crs of the station from the name."""

    with open("crs.json", "r", encoding="utf-8") as f:
        crs_data = json.load(f)

    crs_matches = []

    for station in crs_data:
        if station_name.title() in station["name"]:
            crs_matches.append(station["crs"])

    if len(crs_matches) == 1:
        return crs_matches[0]
    if len(crs_matches) > 1:
        raise ValueError(
            f"'{station_name.title()}' matches with more than 1 station: {crs_matches}")
    if len(crs_matches) == 0:
        raise ValueError(
            f"'{station_name.title()}' does not match any existing station"
        )


def get_station_data(session: requests.Session,
                     station_name: str = None,
                     user_crs: str = None) -> dict:
    """Returns the data from the station provided."""

    # if the user provided a crs they know
    if user_crs:
        rtt_url = f"https://api.rtt.io/api/v1/json/search/{user_crs}"

        response = session.get(url=rtt_url).json()

        return response

    # instead get the crs from the user known station name

    if station_name is None:
        raise TypeError("Cannot leave both crs and station name empty.")

    crs = get_crs(station_name)

    rtt_url = f"https://api.rtt.io/api/v1/json/search/{crs}"

    response = session.get(url=rtt_url).json()

    return response


def get_service_details(session: requests.Session,
                        station_crs: str) -> list[str]:
    """Returns a list of service uids with their origins/destinations
       from services passing through a given station."""

    rtt_url = f"https://api.rtt.io/api/v1/json/search/{station_crs}"

    response = session.get(url=rtt_url).json()

    service_list = []

    for service in response["services"]:

        service_dict = {}

        service_dict["service_uid"] = service["serviceUid"]
        service_dict["origin_station"] = service["locationDetail"]["origin"][0]["description"]
        service_dict["destination_station"] = \
            service["locationDetail"]["destination"][0]["description"]
        service_dict["operator_name"] = service["atocName"]

        service_list.append(service_dict)

    return service_list


def get_service_arrival_details(session: requests.Session, service: dict) -> list[dict]:
    """Returns a list of dictionaries containing
          the arrival details from all stops on that service."""

    today = datetime.now()

    rtt_url = f"https://api.rtt.io/api/v1/json/service/{service['service_uid']}/{today.year}/{today.month:02d}/{today.day:02d}"

    response = session.get(url=rtt_url).json()

    service_arrival_details = []

    arrival_date = response["runDate"]

    for arrival in response["locations"]:
        arrival_dict = {}
        booked_arrival = arrival.get("gbttBookedArrival")
        actual_arrival = arrival.get("realtimeArrival")
        arrival_dict["crs"] = arrival["crs"]
        if booked_arrival:
            arrival_dict["scheduled_arr_time"] = datetime.strptime(
                (arrival_date + booked_arrival), "%Y-%m-%d%H%M")
        else:
            arrival_dict["scheduled_arr_time"] = None
        if actual_arrival:
            arrival_dict["actual_arr_time"] = datetime.strptime(
                (arrival_date + actual_arrival), "%Y-%m-%d%H%M")
        else:
            arrival_dict["actual_arr_time"] = None
        arrival_dict["platform_changed"] = arrival.get("platformChanged")
        arrival_dict["service_uid"] = service["service_uid"]

        service_arrival_details.append(arrival_dict)

    return service_arrival_details


def extract(config: _Environ, station_crs_list: list[str]) -> dict:
    """Extracts the data from the services."""

    basicConfig(level=INFO)

    # get basic authentication for API
    basic_auth = get_basic_auth(ENV)

    session = requests.Session()
    session.auth = basic_auth
    logger.info("Initialised session")

    service_details_list = []

    # get the service details for each station we are looking at
    # this contains the list of every service that passes through each of our stations
    for crs in station_crs_list:
        service_details_list.extend(get_service_details(
            station_crs=crs, session=session))
        logger.info(f"Retrieved service details for {crs}")

    # service_details_list = list(set(service_details_list))
    service_details_list = list({frozenset(d.items())
                                for d in service_details_list})
    service_details_list = [dict(f) for f in service_details_list]

    logger.info("Removed duplicate services")

    arrival_details_list = []

    # get the arrival details for each location each service visits
    for service in service_details_list:
        arrival_details_list.extend(get_service_arrival_details(
            session=session, service=service))
    logger.info("Retrieved arrival details for the services")

    session.close()
    logger.info("Closed session")

    return {
        "services": service_details_list,
        "arrivals": arrival_details_list
    }


if __name__ == "__main__":

    load_dotenv()

    chosen_stations = ["LBG", "STP", "KGX", "SHF", "LST",
                       "BHM", "MAN", "LDS", "BRI", "EDB"]

    DATA = extract(ENV, chosen_stations)
