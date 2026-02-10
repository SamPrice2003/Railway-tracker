"""Small helper script to load stations that have coordinates."""

import pandas as pd

from db import fetch_table


STATIONS_WITH_COORDS_SQL = """
    SELECT
        station_id,
        station_name,
        station_crs,
        latitude,
        longitude
    FROM station
    WHERE latitude IS NOT NULL
      AND longitude IS NOT NULL;
"""


def load_stations_with_coords() -> pd.DataFrame:
    """Load stations that have valid latitude and longitude values."""
    stations = fetch_table(STATIONS_WITH_COORDS_SQL)
    if stations is None:
        return pd.DataFrame()
    return stations


def main() -> None:
    """Run a quick local check and print the first few rows."""
    stations = load_stations_with_coords()
    print(stations.head())


if __name__ == "__main__":
    main()
