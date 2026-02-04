""" The extract script responsible for extracting static data from the RTT api """

# imports
import pandas as pd

import requests
from requests.auth import HTTPBasicAuth

from os import environ as ENV, _Environ, path
from dotenv import load_dotenv

import json

from logging import getLogger, basicConfig, INFO

from datetime import datetime

logger = getLogger(__name__)

# set up basic auth with credentials


def get_basic_auth(config: _Environ):
    """returns a basic auth from credentials"""

    basic = HTTPBasicAuth(
        username=ENV["RTT_USER"], password=ENV["RTT_PASSWORD"])

    return basic


def get_session(auth: HTTPBasicAuth) -> requests.Session:
    """returns a session to make api calls faster"""

    session = requests.Session()

    session.auth = auth

    return session


def get_crs(station_name: str) -> str:
    """returns the crs of the station from the name"""

    with open("crs.json", "r") as f:
        crs_data = json.load(f)

    crs_matches = []

    for station in crs_data:
        if station_name.title() in station["name"]:
            crs_matches.append(station["crs"])

    if len(crs_matches) != 1:
        raise ValueError(
            f"'{station_name.title()}' matches with more than 1 station: {crs_matches}")

    return crs_matches[0]


def get_station_data(session: requests.Session, station_name: str = None, user_crs: str = None) -> dict:
    """returns the data from the station provided"""

    # if the user provided a crs they know
    if user_crs:
        rtt_url = f"https://api.rtt.io/api/v1/json/search/{user_crs}"

        # response = requests.get(url=rtt_url, auth=authorisation)
        response = session.get(url=rtt_url).json()

        return response

    # instead get the crs from the user known station name
    else:
        if station_name is None:
            raise TypeError("Cannot leave both crs and station name empty")

        crs = get_crs(station_name)

        rtt_url = f"https://api.rtt.io/api/v1/json/search/{crs}"

        # response = requests.get(url=rtt_url, auth=authorisation)
        response = session.get(url=rtt_url).json()

        return response


def get_service_details(session: requests.Session, station_crs: str) -> list[str]:
    """returns a list of service uids with their origins/destinations from services passing through a given station"""

    rtt_url = f"https://api.rtt.io/api/v1/json/search/{station_crs}"

    # response = requests.get(url=rtt_url, auth=authorisation).json()
    response = session.get(url=rtt_url).json()

    service_list = []

    for service in response["services"]:

        service_dict = {}

        service_dict["service_uid"] = service["serviceUid"]
        service_dict["origin_station"] = service["locationDetail"]["origin"][0]["description"]
        service_dict["destination_station"] = service["locationDetail"]["destination"][0]["description"]

        service_list.append(service_dict)

    return service_list


def get_service_arrival_details(session: requests.Session, service: dict) -> list[dict]:
    """returns a list of dictionaries containing the arrival details from all stops on that service"""

    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    rtt_url = f"https://api.rtt.io/api/v1/json/service/{service['service_uid']}/{year}/{month:02d}/{day:02d}"

    # response = requests.get(url=rtt_url, auth=authorisation).json()
    response = session.get(url=rtt_url).json()

    service_arrival_details = []

    rundate = response["runDate"]

    for arrival in response["locations"]:
        arrival_dict = {}
        arrival_dict["crs"] = arrival["crs"]
        if arrival.get("gbttBookedArrival"):
            arrival_dict["scheduled_arr_time"] = datetime.strptime(
                (rundate + arrival.get("gbttBookedArrival")), "%Y-%m-%d%H%M")
        else:
            arrival_dict["scheduled_arr_time"] = None
        if arrival.get("realtimeArrival"):
            arrival_dict["actual_arr_time"] = datetime.strptime(
                (rundate + arrival.get("realtimeArrival")), "%Y-%m-%d%H%M")
        else:
            arrival_dict["actual_arr_time"] = None
        arrival_dict["platform_changed"] = arrival.get("platformChanged")
        arrival_dict["service_uid"] = service["service_uid"]

        service_arrival_details.append(arrival_dict)

    return service_arrival_details


def remove_duplicates(data: list[dict]) -> list[dict]:
    """removes all duplicate entries from a list of dictionaries"""

    for d in data:
        while data.count(d) > 1:
            data.remove(d)

    return data


def extract(config: _Environ, station_crs_list: list[str]) -> dict:
    """extracts the data from the services"""

    basicConfig(level=INFO)

    # get basic authentication for API
    basic = get_basic_auth(ENV)

    # get the session used
    session = get_session(auth=basic)
    logger.info("Initialised session")

    # initialise empty service details list
    service_details_list = []

    # get the service details for each station we are looking at
    # this contains the list of every service that passes through each of our stations
    for crs in station_crs_list:
        service_details_list.extend(get_service_details(
            station_crs=crs, session=session))
        logger.info(f"Retrieved service details for {crs}")

    # remove any duplicate services which may have gone through
    # multiple of the stations we specified
    service_details_list = remove_duplicates(service_details_list)
    logger.info("Removed duplicate services")

    # initialise arrivals list information
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

    # load environment variables
    load_dotenv()

    CHOSEN_STATIONS = ["LBG", "STP", "KGX", "SHF", "LST"]

    DATA = extract(ENV, CHOSEN_STATIONS)
