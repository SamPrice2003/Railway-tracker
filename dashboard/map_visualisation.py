"""Map helpers for showing station lateness on a Folium map."""

from datetime import date

import folium
import pandas as pd

from database_connection import fetch_dataframe

UK_center_coordinates = (54.5, -2.5)


STATIONS_SQL = """
    SELECT
        station_id,
        station_name,
        station_crs,
        latitude,
        longitude
    FROM station;
"""

ARRIVALS_FOR_DAY_SQL = """
    SELECT
        a.arrival_station_id AS arrival_station_id,
        (a.arrival_date + a.scheduled_time) AS scheduled_arr_time,
        (a.arrival_date + a.actual_time) AS actual_arr_time,
        GREATEST(
            EXTRACT(EPOCH FROM (
                (a.arrival_date + a.actual_time) - (a.arrival_date + a.scheduled_time)
            )) / 60.0,
            0
        ) AS delay_minutes
    FROM arrival AS a
    WHERE a.arrival_date = %s;
"""


def load_stations() -> pd.DataFrame:
    """Load station details from the database."""
    return fetch_dataframe(STATIONS_SQL)


def load_arrivals_for_day(chosen_day: date) -> pd.DataFrame:
    """Load arrivals for a single day and calculate delay minutes."""
    rows = fetch_dataframe(ARRIVALS_FOR_DAY_SQL, values=(chosen_day,))
    if rows is None or rows.empty:
        return pd.DataFrame()

    data = rows.copy()
    data["scheduled_arr_time"] = pd.to_datetime(
        data["scheduled_arr_time"], errors="coerce")
    data["actual_arr_time"] = pd.to_datetime(
        data["actual_arr_time"], errors="coerce")
    return data


def build_station_lateness(stations: pd.DataFrame, arrivals: pd.DataFrame) -> pd.DataFrame:
    """Group arrivals into station level lateness percentages."""
    if arrivals is None or arrivals.empty:
        return pd.DataFrame()

    grouped = (
        arrivals.groupby("arrival_station_id", as_index=False)
        .agg(arrivals=("arrival_station_id", "count"), percent_late=("is_late", "mean"))
    )

    grouped["percent_late"] = grouped["percent_late"].fillna(0) * 100.0

    stations_clean = stations.copy()
    stations_clean["station_id"] = pd.to_numeric(
        stations_clean["station_id"], errors="coerce")

    merged = grouped.merge(
        stations_clean[["station_id", "station_name",
                        "station_crs", "latitude", "longitude"]],
        left_on="arrival_station_id",
        right_on="station_id",
        how="left",
    )

    return merged.dropna(subset=["latitude", "longitude"])


def pick_colour(percent_late: float) -> str:
    """Pick a marker colour based on the late percentage."""
    if percent_late >= 50:
        return "red"
    if percent_late >= 25:
        return "orange"
    if percent_late >= 10:
        return "yellow"
    return "green"


def add_map_legend(map_obj: folium.Map) -> None:
    """Add a small legend to the bottom left of the map."""
    legend_html = """
    <div style="
      position: fixed;
      bottom: 30px;
      left: 30px;
      width: 240px;
      z-index: 9999;
      background: white;
      padding: 10px;
      border: 2px solid #777;
      border-radius: 6px;
      font-size: 12px;
    ">
      <b>% Late per station</b><br>
      <span style="color:green;">●</span> &lt; 10%<br>
      <span style="color:yellow;">●</span> 10–25%<br>
      <span style="color:orange;">●</span> 25–50%<br>
      <span style="color:red;">●</span> &gt; 50%<br>
    </div>
    """
    map_obj.get_root().html.add_child(folium.Element(legend_html))


def pick_map_center(stations: pd.DataFrame, lateness: pd.DataFrame) -> tuple[float, float]:
    """Pick a sensible map center based on available coordinates."""
    if lateness is not None and not lateness.empty:
        lat = lateness["latitude"].mean()
        lon = lateness["longitude"].mean()
        if pd.notna(lat) and pd.notna(lon):
            return float(lat), float(lon)

    base = stations.dropna(subset=["latitude", "longitude"])
    if not base.empty:
        return float(base["latitude"].mean()), float(base["longitude"].mean())

    return UK_center_coordinates


def build_map(stations: pd.DataFrame, lateness: pd.DataFrame) -> folium.Map:
    """Build a Folium map using station lateness values."""
    center_lat, center_lon = pick_map_center(stations, lateness)

    map_obj = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=6,
        tiles="CartoDB positron",
    )

    if lateness is None or lateness.empty:
        add_map_legend(map_obj)
        return map_obj

    for _, row in lateness.iterrows():
        arrivals_count = int(row["arrivals"])
        late_percent = float(row["percent_late"])
        radius = min(14, max(4, arrivals_count**0.5))

        name = row.get("station_name", "")
        crs = row.get("station_crs", "")
        tooltip = f"{name} ({crs}) • {late_percent:.0f}% late"
        popup = f"Arrivals: {arrivals_count}<br>% late: {late_percent:.1f}%"

        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=radius,
            color=pick_colour(late_percent),
            fill=True,
            fill_opacity=0.75,
            tooltip=tooltip,
            popup=popup,
        ).add_to(map_obj)

    add_map_legend(map_obj)
    return map_obj


# def main() -> None:
#     """Build a test HTML map for today and save it locally."""
#     stations = load_stations()
#     arrivals = load_arrivals_for_day(date.today())
#     if arrivals.empty:
#         print("No arrivals found for today.")
#         return

#     arrivals = arrivals.copy()
#     arrivals["is_late"] = arrivals["delay_minutes"] >= 2

#     lateness = build_station_lateness(stations, arrivals)
#     map_obj = build_map(stations, lateness)
#     map_obj.save("/temp/station_lateness_map.html")

if __name__ == "__main__":
  ...
