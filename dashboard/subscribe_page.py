"""Subscribe page where a user can sign up for station alerts."""
# pylint: disable=broad-exception-caught
from re import match

import pandas as pd
import streamlit as st

from database_connection import fetch_dataframe, run_change, run_change_returning


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
    return match(pattern, email.strip()) is not None


@st.cache_data(ttl=300)
def load_station_list() -> pd.DataFrame:
    """Load stations for the dropdown and cache for a short time."""
    stations = fetch_dataframe("""
    SELECT
        station_id,
        station_name,
        station_crs
    FROM station
    ORDER BY station_name;
    """)
    if stations is None or stations.empty:
        return pd.DataFrame()
    return stations


def get_or_create_customer_id(user_email: str) -> int:
    email = user_email.strip().lower()

    df = fetch_dataframe(
        "SELECT customer_id FROM customer WHERE customer_email = %s;",
        values=(email,),
    )
    if df is not None and not df.empty:
        return int(df.iloc[0]["customer_id"])

    df = run_change_returning(
        """
        INSERT INTO customer (customer_email)
        VALUES (%s)
        RETURNING customer_id;
        """,
        values=(email,),
    )
    if df is None or df.empty:
        raise ValueError("Failed to create customer.")
    return int(df.iloc[0]["customer_id"])


def save_subscription(user_email: str, station_id: int, subscription_type: str = "station") -> bool:
    try:
        customer_id = get_or_create_customer_id(user_email)
        run_change(
            """
            INSERT INTO subscription (customer_id, station_id, subscription_type)
            VALUES (%s, %s, %s);
            """,
            values=(customer_id, int(station_id), subscription_type),
        )
        return True
    except Exception:
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
    stations["label"] = (
        stations["station_name"] + " (" + stations["station_crs"] + ")"
    )

    with st.form("subscribe_form", clear_on_submit=False):
        email = st.text_input("Your email")

        chosen_label = st.selectbox(
            "Choose a station",
            stations["label"].tolist(),
        )

        subscribe_daily = st.checkbox(
            "Subscribe to daily summary report"
        )

        submitted = st.form_submit_button("Subscribe")

    if submitted:
        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
            return

        chosen_row = stations[stations["label"] == chosen_label].head(1)
        if chosen_row.empty:
            st.error("Could not find that station, please try again.")
            return

        station_id = int(chosen_row.iloc[0]["station_id"])

        station_ok = save_subscription(
            email,
            station_id,
            subscription_type="station",
        )

        report_ok = True
        if subscribe_daily:
            report_ok = save_subscription(
                email,
                station_id,
                subscription_type="report",
            )

        if station_ok and report_ok:
            st.success("Subscription saved successfully.")
        else:
            st.error("Subscription failed, you may already be subscribed.")

    st.markdown(
        "<a href='?view=unsubscribe'>Unsubscribe</a>",
        unsafe_allow_html=True,
    )
