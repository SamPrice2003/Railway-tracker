"Script which extracts data from the National Rail API."

from os import environ as ENV

from dotenv import load_dotenv
from requests import post


AUTH_ENDPOINT = "https://opendata.nationalrail.co.uk/authenticate"


def get_auth_token(username: str, password: str) -> str:
    """Returns an authentication token for the National Rail API
    if username and password is correct."""

    response = post(AUTH_ENDPOINT, data={
        "username": username,
        "password": password
    }).json()

    return response["token"]


if __name__ == "__main__":

    load_dotenv()

    token = get_auth_token(
        ENV["NATIONAL_RAIL_API_USERNAME"], ENV["NATIONAL_RAIL_API_PASSWORD"])
