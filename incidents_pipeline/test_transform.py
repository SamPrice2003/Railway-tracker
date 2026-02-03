"""Script for testing transform.py"""

from transform import get_filtered_message


def test_get_filtered_message_valid_columns(test_incident_message):
    filtered_message = get_filtered_message(test_incident_message)

    expected_columns = set(["summary", "operators",
                           "incident_start", "incident_end", "url", "planned"])
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
