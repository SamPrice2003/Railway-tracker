"""Test fixtures for the metrics pipeline tests."""

# pylint:skip-file

import pytest


@pytest.fixture
def test_mock_crs_file():
    return """[
        {
            "name": "Abbey Wood (London) Rail Station",
            "crs": "ABW"
        },
        {
            "name": "Albany Park Rail Station",
            "crs": "AYP"
        },
        {
            "name": "Kew Gardens Rail Station",
            "crs": "KWG"
        },
        {
            "name": "Rochester Rail Station",
            "crs": "RTR"
        },
        {
            "name": "Rochester Rail Station",
            "crs": "RTR"
        },
        {
            "name": "Yetminster Rail Station",
            "crs": "YET"
        }
    ]"""


@pytest.fixture
def test_mock_rtt_api_crs_call():
    return """{
        "location": {
            "name": "London Bridge",
            "crs": "LBG",
            "tiploc": [
                "LNDNBDC",
                "LNDNBDE",
                "LNDNBDG"
            ],
            "country": "gb",
            "system": "nr"
        },
        "filter": null,
        "services": [
            {
                "locationDetail": {
                    "realtimeActivated": true,
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
                            "workingTime": "105500",
                            "publicTime": "1055"
                        }
                    ],
                    "isCall": true,
                    "isPublicCall": true,
                    "realtimeArrival": "1052",
                    "realtimeArrivalActual": false,
                    "realtimeDeparture": "1054",
                    "realtimeDepartureActual": false,
                    "platform": "3",
                    "platformConfirmed": false,
                    "platformChanged": false,
                    "displayAs": "CALL"
                },
                "serviceUid": "P72907",
                "runDate": "2026-02-12",
                "trainIdentity": "2P23",
                "runningIdentity": "2P23",
                "atocCode": "SE",
                "atocName": "Southeastern",
                "serviceType": "train",
                "isPassenger": true
            }
        ]}"""
