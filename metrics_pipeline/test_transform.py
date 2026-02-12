"""Testing for transform.py"""

# pylint:skip-file

import pandas as pd

from transform import get_station_name_dict, assign_station_id_to_arrival, assign_operator_id_to_service


def test_get_station_name_dict_valid():
    test_station_crs_list = [
        {
            "station_name": "Albany Park Rail Station",
            "station_id": 1
        },
        {
            "station_name": "Abbey Wood Rail Station",
            "station_id": 2
        }
    ]

    assert get_station_name_dict(test_station_crs_list) == {
        "Albany Park": 1,
        "Abbey Wood": 2
    }


def test_get_station_name_dict_valid_2():
    test_station_crs_list = [
        {
            "station_name": "Yetminster",
            "station_id": 23
        },
        {
            "station_name": "Heathrow Rail Station",
            "station_id": 4
        }
    ]

    assert get_station_name_dict(test_station_crs_list) == {
        "Yetminster": 23,
        "Heathrow": 4
    }


def test_assign_station_id_to_arrival_valid():
    test_station_crs_list = [
        {
            "station_crs": "LBG",
            "station_id": 2
        },
        {
            "station_crs": "HTX",
            "station_id": 4
        }
    ]

    test_df = pd.DataFrame(data={"crs": ["LBG", "HTX"]})

    target_df = pd.DataFrame(
        data={"crs": ["LBG", "HTX"], "arrival_station_id": [2, 4]})

    assert pd.concat([assign_station_id_to_arrival(
        test_df, test_station_crs_list), target_df]).drop_duplicates(keep=False).empty == True


def test_assign_station_id_to_arrival_valid_2():
    test_station_crs_list = [
        {
            "station_crs": "RIH",
            "station_id": 45
        },
        {
            "station_crs": "POW",
            "station_id": 7
        }
    ]

    test_df = pd.DataFrame(data={"crs": ["RIH", "POW"]})

    target_df = pd.DataFrame(
        data={"crs": ["RIH", "POW"], "arrival_station_id": [45, 7]})

    assert pd.concat([assign_station_id_to_arrival(
        test_df, test_station_crs_list), target_df]).drop_duplicates(keep=False).empty == True


def test_assign_operator_id_to_service_valid():
    test_operator_name_list = [
        {
            "operator_name": "Avanti West Coast",
            "operator_id": 2
        },
        {
            "operator_name": "Southeastern",
            "operator_id": 8
        }
    ]

    test_df = pd.DataFrame(
        data={"operator_name": ["Southeastern", "Avanti West Coast"]})

    target_df = pd.DataFrame(
        data={"operator_name": ["Southeastern", "Avanti West Coast"], "operator_id": [8, 2], })

    assert pd.concat([assign_operator_id_to_service(
        test_df, test_operator_name_list), target_df]).drop_duplicates(keep=False).empty == True


def test_assign_operator_id_to_service_valid_2():
    test_operator_name_list = [
        {
            "operator_name": "c2c",
            "operator_id": 200
        },
        {
            "operator_name": "Southern",
            "operator_id": 81
        }
    ]

    test_df = pd.DataFrame(
        data={"operator_name": ["Southern", "c2c"]})

    target_df = pd.DataFrame(
        data={"operator_name": ["Southern", "c2c"], "operator_id": [81, 200], })

    assert pd.concat([assign_operator_id_to_service(
        test_df, test_operator_name_list), target_df]).drop_duplicates(keep=False).empty == True
