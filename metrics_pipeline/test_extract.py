"""Script for testing extract.py"""

# pylint:skip-file

import pytest
from unittest.mock import patch, mock_open

from requests import Session, Response

from extract import get_crs, get_station_data, get_service_details


def test_get_crs_correct(test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    with patch("builtins.open", mocked_open_function):
        assert get_crs("Albany Park Rail Station") == "AYP"


def test_get_crs_correct_2(test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    with patch("builtins.open", mocked_open_function):
        assert get_crs("Yetminster Rail Station") == "YET"


def test_get_crs_incorrect(test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    with patch("builtins.open", mocked_open_function):
        with pytest.raises(ValueError) as e:
            assert get_crs("Nope")
            assert "does not match any existing station" in str(e.value)


def test_get_crs_duplicate(test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    with patch("builtins.open", mocked_open_function):
        with pytest.raises(ValueError) as e:
            assert get_crs("Rochester Rail Station")
            assert "matches with more than 1 station" in str(e.value)


@patch.object(Session, "get")
def test_get_station_data_with_name(mock_get, test_mock_rtt_api_crs_call, test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    response = Response()
    response._content = bytes(test_mock_rtt_api_crs_call, encoding="utf-8")

    mock_get.return_value = response

    with patch("builtins.open", mocked_open_function):
        assert get_station_data(Session(), "London Bridge Rail Station") == {
            "location":
            {
                "name": "London Bridge",
                "crs": "LBG",
                "tiploc":
                ["LNDNBDC", "LNDNBDE", "LNDNBDG"],
                "country": "gb",
                "system": "nr"
            },
            "filter": None,
            "services":
                [
                    {
                        "locationDetail":
                        {
                            "realtimeActivated": True,
                            "tiploc": "LNDNBDE",
                            "crs": "LBG",
                            "description": "London Bridge",
                            "gbttBookedArrival": "1049",
                            "gbttBookedDeparture": "1051",
                            "origin": [
                                {
                                    "tiploc": "CANONST",
                                    "description": "London Cannon Street",
                                    "workingTime": "092600",
                                    "publicTime": "0926"
                                }
                            ],
                            "destination": [
                                {
                                    "tiploc": "CANONST",
                                    "description": "London Cannon Street",
                                    "workingTime": "105500", "publicTime": "1055"
                                }
                            ],
                            "isCall": True,
                            "isPublicCall": True,
                            "realtimeArrival": "1052",
                            "realtimeArrivalActual": False,
                            "realtimeDeparture": "1054",
                            "realtimeDepartureActual": False,
                            "platform": "3",
                            "platformConfirmed": False,
                            "platformChanged": False,
                            "displayAs": "CALL"
                        },
                        "serviceUid": "P72907",
                        "runDate": "2026-02-12",
                        "trainIdentity": "2P23",
                        "runningIdentity": "2P23",
                        "atocCode": "SE",
                        "atocName": "Southeastern",
                        "serviceType": "train",
                        "isPassenger": True
                    }
            ]
        }


@patch.object(Session, "get")
def test_get_station_data_with_crs(mock_get, test_mock_rtt_api_crs_call, test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    response = Response()
    response._content = bytes(test_mock_rtt_api_crs_call, encoding="utf-8")

    mock_get.return_value = response

    with patch("builtins.open", mocked_open_function):
        assert get_station_data(Session(), user_crs="LBG") == {
            "location":
            {
                "name": "London Bridge",
                "crs": "LBG",
                "tiploc":
                ["LNDNBDC", "LNDNBDE", "LNDNBDG"],
                "country": "gb",
                "system": "nr"
            },
            "filter": None,
            "services":
                [
                    {
                        "locationDetail":
                        {
                            "realtimeActivated": True,
                            "tiploc": "LNDNBDE",
                            "crs": "LBG",
                            "description": "London Bridge",
                            "gbttBookedArrival": "1049",
                            "gbttBookedDeparture": "1051",
                            "origin": [
                                {
                                    "tiploc": "CANONST",
                                    "description": "London Cannon Street",
                                    "workingTime": "092600",
                                    "publicTime": "0926"
                                }
                            ],
                            "destination": [
                                {
                                    "tiploc": "CANONST",
                                    "description": "London Cannon Street",
                                    "workingTime": "105500", "publicTime": "1055"
                                }
                            ],
                            "isCall": True,
                            "isPublicCall": True,
                            "realtimeArrival": "1052",
                            "realtimeArrivalActual": False,
                            "realtimeDeparture": "1054",
                            "realtimeDepartureActual": False,
                            "platform": "3",
                            "platformConfirmed": False,
                            "platformChanged": False,
                            "displayAs": "CALL"
                        },
                        "serviceUid": "P72907",
                        "runDate": "2026-02-12",
                        "trainIdentity": "2P23",
                        "runningIdentity": "2P23",
                        "atocCode": "SE",
                        "atocName": "Southeastern",
                        "serviceType": "train",
                        "isPassenger": True
                    }
            ]
        }


@patch.object(Session, "get")
def test_get_service_details(mock_get, test_mock_rtt_api_crs_call, test_mock_crs_file):
    mocked_open_function = mock_open(read_data=test_mock_crs_file)

    response = Response()
    response._content = bytes(test_mock_rtt_api_crs_call, encoding="utf-8")

    mock_get.return_value = response
    with patch("builtins.open", mocked_open_function):
        assert get_service_details(Session(), "LBG") == [
            {
                "service_uid": "P72907",
                "origin_station": "London Cannon Street",
                "destination_station": "London Cannon Street",
                "operator_name": "Southeastern"
            }
        ]
