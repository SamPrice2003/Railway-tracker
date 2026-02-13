"""Script for testing transform.py"""

# pylint:skip-file

from datetime import datetime, timezone

from incidents_transform import get_filtered_message, get_corrected_types, get_transformed_message, get_services_affected


def test_get_filtered_message_valid_columns(test_incident_message):
    filtered_message = get_filtered_message(test_incident_message)

    expected_columns = set(["summary", "operators",
                           "incident_start", "incident_end", "url", "planned", "services_affected"])
    actual_columns = set(filtered_message.keys())

    assert expected_columns == actual_columns


def test_get_filtered_message_valid_values(test_incident_message):
    filtered_message = get_filtered_message(test_incident_message)

    assert filtered_message["summary"] == "Disruption between Arbroath and Aberdeen expected until 18:00"
    assert filtered_message["operators"] == ["LNER", "ScotRail"]
    assert filtered_message["incident_start"] == "2026-02-03T14:05:00.000Z"
    assert filtered_message["incident_end"] == "2026-02-03T18:05:00.000Z"
    assert filtered_message["url"] == "https://www.nationalrail.co.uk/service-disruptions/arbroath-20260203/"
    assert filtered_message["planned"] == "true"


def test_get_corrected_types_valid_types():
    test_dict = {
        "incident_start": "2026-02-03T14:05:00.000Z",
        "incident_end": "2026-02-03T18:05:00.000Z",
        "planned": "true"
    }

    actual_dict = get_corrected_types(test_dict)

    assert isinstance(actual_dict["incident_start"], datetime)
    assert isinstance(actual_dict["incident_end"], datetime)
    assert isinstance(actual_dict["planned"], bool)


def test_get_corrected_types_valid_values():
    test_dict = {
        "incident_start": "2026-02-03T14:05:00.000Z",
        "incident_end": "2026-02-03T18:05:00.000Z",
        "planned": "false"
    }

    actual_dict = get_corrected_types(test_dict)

    assert actual_dict["incident_start"] == datetime.fromisoformat(
        test_dict["incident_start"])
    assert actual_dict["incident_end"] == datetime.fromisoformat(
        test_dict["incident_end"])
    assert actual_dict["planned"] == False


def test_get_transformed_message_contents(test_incident_message):
    test_message = get_transformed_message(test_incident_message)

    assert test_message == {
        "summary": "Disruption between Arbroath and Aberdeen expected until 18:00",
        "operators": ["LNER", "ScotRail"],
        "incident_start": datetime(2026, 2, 3, 14, 5, tzinfo=timezone.utc),
        "incident_end": datetime(2026, 2, 3, 18, 5, tzinfo=timezone.utc),
        "url": "https://www.nationalrail.co.uk/service-disruptions/arbroath-20260203/",
        "planned": True,
        "services_affected": [
            {
                "origin_station": "London Kings Cross",
                "destination_station": "Aberdeen"
            },
            {
                "origin_station": "Glasgow Queen Street",
                "destination_station": "Aberdeen"
            },
            {
                "origin_station": "Glasgow Queen Street",
                "destination_station": "Inverness"
            },
            {
                "origin_station": "Dundee",
                "destination_station": "Arbroath"
            }
        ]
    }


def test_get_services_affected_simple():
    services_affected = get_services_affected(
        "<p>Between London Victoria and Oxted / East Grinstead</p>")

    assert services_affected == [
        {
            "origin_station": "London Victoria",
            "destination_station": "East Grinstead"
        }
    ]


def test_get_services_affected_complex(test_incident_message):
    services_affected = get_services_affected(
        test_incident_message["Affects"]["RoutesAffected"])

    assert services_affected == [
        {
            "origin_station": "London Kings Cross",
            "destination_station": "Aberdeen"
        },
        {
            "origin_station": "Glasgow Queen Street",
            "destination_station": "Aberdeen"
        },
        {
            "origin_station": "Glasgow Queen Street",
            "destination_station": "Inverness"
        },
        {
            "origin_station": "Dundee",
            "destination_station": "Arbroath"
        }
    ]
