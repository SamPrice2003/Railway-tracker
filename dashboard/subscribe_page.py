"""Subscribe page where a user can sign up for station alerts."""

import re

import pandas as pd
import streamlit as st

from db import fetch_table, run_change

STATIONS_SQL = """
    SELECT
        station_id,
        station_name,
        station_crs
    FROM station
    ORDER BY station_name;
"""

INSERT_SUB_SQL = """
    INSERT INTO subscription (customer_id, station_id)
    VALUES (%s, %s);
"""


def add_subscribe_css() -> None:
    """Add small CSS used on the subscribe page."""
    st.markdown(
        """
        <style>
          .ss-blue { color: #2563eb; }
          div[data-testid="stMetricValue"] { color: #2563eb; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def is_valid_email(email: str) -> bool:
    """Check if an email looks valid using a simple pattern."""
    if not email:
        return False
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email.strip()) is not None


@st.cache_data(ttl=300)
def load_station_list() -> pd.DataFrame:
    """Load stations for the dropdown and cache for a short time."""
    stations = fetch_table(STATIONS_SQL)
    if stations is None or stations.empty:
        return pd.DataFrame()
    return stations


def save_subscription(user_email: str, station_id: int) -> bool:
    """Save a subscription row and return True if it worked."""
    try:
        run_change(INSERT_SUB_SQL, values=(
            user_email.strip().lower(), int(station_id)))
        return True
    except Exception:  # pylint: disable=broad-exception-caught
        return False


def render_subscribe_page() -> None:
    """Render the subscribe page."""
    add_subscribe_css()

    st.title("Subscribe")
    st.markdown(
        "<p class='ss-blue'>Get alerts for delays and incidents on your chosen station.</p>",
        unsafe_allow_html=True,
    )

    stations = load_station_list()
    if stations.empty:
        st.warning("No stations available right now.")
        st.markdown("<a href='?view=unsubscribe'>Unsubscribe</a>",
                    unsafe_allow_html=True)
        return

    stations = stations.copy()
    stations["label"] = stations["station_name"] + \
        " (" + stations["station_crs"] + ")"

    with st.form("subscribe_form", clear_on_submit=False):
        email = st.text_input("Your email")
        chosen_label = st.selectbox(
            "Choose a station", stations["label"].tolist())
        submitted = st.form_submit_button("Subscribe")

    if submitted:
        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
        else:
            chosen_row = stations[stations["label"] == chosen_label].head(1)
            if chosen_row.empty:
                st.error("Could not find that station, please try again.")
            else:
                station_id = int(chosen_row.iloc[0]["station_id"])
                ok = save_subscription(email, station_id)

                if ok:
                    st.success("Subscribed successfully.")
                else:
                    st.error(
                        "Subscription failed, you may already be subscribed.")

    st.markdown("<a href='?view=unsubscribe'>Unsubscribe</a>",
                unsafe_allow_html=True)
