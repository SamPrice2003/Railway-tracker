"""Incidents page with simple charts and basic impact numbers."""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from db import fetch_table


INCIDENTS_SQL = """
    SELECT
        incident_id,
        summary,
        incident_start,
        incident_end,
        url,
        planned
    FROM incident
    ORDER BY incident_start DESC;
"""

USERS_AFFECTED_SQL = """
    SELECT
        COUNT(DISTINCT sub.customer_id) AS users_affected,
        COUNT(DISTINCT sub.station_id) AS stations_with_subscribers
    FROM incident AS i
    JOIN service_assignment AS sa
        ON sa.incident_id = i.incident_id
    JOIN arrival AS a
        ON a.service_id = sa.service_id
    JOIN subscription AS sub
        ON sub.station_id = a.arrival_station_id
    WHERE i.incident_start <= NOW()
      AND (i.incident_end IS NULL OR i.incident_end >= NOW())
      AND (
            (a.arrival_date + a.actual_time) >= NOW() - INTERVAL '24 hours'
         OR (a.arrival_date + a.scheduled_time) >= NOW() - INTERVAL '24 hours'
      );
"""


def add_incidents_css() -> None:
    """Add small CSS tweaks used on the incidents page."""
    st.markdown(
        """
        <style>
          .ss-blue { color: #2563eb; }
          div[data-testid="stMetricValue"] { color: #2563eb; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_blue_heading(text: str) -> None:
    """Show a blue heading using simple HTML."""
    st.markdown(f"<h3 class='ss-blue'>{text}</h3>", unsafe_allow_html=True)


def to_bool(values: pd.Series | None) -> pd.Series:
    """Turn a column into boolean values in a safe way."""
    if values is None:
        return pd.Series(dtype="boolean")

    if str(values.dtype).lower() in {"bool", "boolean"}:
        return values.astype("boolean")

    as_text = values.astype("string").str.strip().str.lower()
    yes_values = {"true", "t", "1", "yes"}
    return as_text.map(lambda item: item in yes_values).astype("boolean")


def load_incident_rows() -> pd.DataFrame:
    """Load incidents and add a few extra columns used by the page."""
    data = fetch_table(INCIDENTS_SQL)
    if data is None or data.empty:
        return pd.DataFrame()

    data["incident_start"] = pd.to_datetime(
        data["incident_start"], errors="coerce")
    data["incident_end"] = pd.to_datetime(
        data["incident_end"], errors="coerce")
    data["planned"] = to_bool(data.get("planned"))

    now_time = pd.Timestamp.now()
    data["is_active"] = data["incident_start"].notna() & (
        data["incident_end"].isna() | (data["incident_end"] >= now_time)
    )

    data["duration_mins"] = (
        (data["incident_end"] - data["incident_start"]).dt.total_seconds() / 60.0
    )

    return data


def load_users_affected() -> tuple[int, int]:
    """Load estimated impacted users and subscribed stations for active incidents."""
    data = fetch_table(USERS_AFFECTED_SQL)
    if data is None or data.empty:
        return 0, 0

    first_row = data.iloc[0]
    users = int(first_row.get("users_affected", 0) or 0)
    stations = int(first_row.get("stations_with_subscribers", 0) or 0)
    return users, stations


def show_planned_donut(planned_count: int, unplanned_count: int) -> None:
    """Show a donut chart for planned vs unplanned incidents."""
    chart = go.Figure(
        data=[
            go.Pie(
                labels=["Planned", "Unplanned"],
                values=[planned_count, unplanned_count],
                hole=0.65,
            )
        ]
    )
    chart.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(chart, use_container_width=True)


def show_users_section() -> None:
    """Show the users affected section using two metrics."""
    show_blue_heading("Users affected")
    st.markdown(
        "<p class='ss-blue'>Estimated impacted users based on active incidents.</p>",
        unsafe_allow_html=True,
    )

    users, stations = load_users_affected()

    users_text = "None" if users == 0 else str(users)
    stations_text = "None" if stations == 0 else str(stations)

    left, right = st.columns(2)
    with left:
        st.metric("Users affected (active incidents)", users_text)
    with right:
        st.metric("Impacted subscribed stations", stations_text)


def render_incidents_page() -> None:
    """Render the full incidents page."""
    add_incidents_css()

    st.title("Live incidents")
    st.markdown(
        "<p class='ss-blue'>Operational incidents and estimated subscriber exposure.</p>",
        unsafe_allow_html=True,
    )

    incidents = load_incident_rows()
    if incidents.empty:
        st.info("No incidents available.")
        return

    active_count = int(incidents["is_active"].sum())

    planned_rate = float(incidents["planned"].fillna(False).astype(int).mean())

    if incidents["duration_mins"].notna().any():
        avg_duration = float(incidents["duration_mins"].dropna().mean())
    else:
        avg_duration = 0.0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Active incidents", active_count)
    with col2:
        st.metric("Planned share", f"{planned_rate * 100:.0f}%")
    with col3:
        st.metric("Avg duration (mins)", f"{avg_duration:.0f}")

    st.divider()

    show_blue_heading("Planned vs unplanned")
    planned_count = int(incidents["planned"].fillna(False).sum())
    unplanned_count = int(len(incidents) - planned_count)
    show_planned_donut(planned_count, unplanned_count)

    st.divider()

    show_blue_heading("Active incidents")
    active_only = st.toggle("Show active only", value=True)
    shown = incidents[incidents["is_active"]] if active_only else incidents

    cols = ["incident_id", "summary", "incident_start",
            "incident_end", "planned", "url"]
    st.dataframe(shown[cols], use_container_width=True, hide_index=True)

    st.divider()
    show_users_section()
