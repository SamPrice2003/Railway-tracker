"""Subscribe page where a user can sign up for station alerts."""
# pylint: disable=broad-exception-caught
from os import environ as ENV

from re import match
from json import dumps, loads
from dotenv import load_dotenv

from boto3 import client
import pandas as pd
import streamlit as st

from database_connection import fetch_dataframe, run_change, run_change_returning


def get_sns_client() -> client:
    """Returns an AWS SNS client."""

    return client(
        "sns",
        aws_access_key_id=ENV["ACCESS_KEY_AWS"],
        aws_secret_access_key=ENV["SECRET_KEY_AWS"]
    )


def get_sns_topic_arn() -> str:
    """Returns the SNS topic ARN. Returns the ARN if it already exists.
    Creates a new SNS topic and returns the ARN if it does not already exist."""

    sns_client = get_sns_client()

    response = sns_client.create_topic(
        Name=ENV["SNS_TOPIC"]
    )

    return response["TopicArn"]


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


def subscribe_customer(user_email: str, station_name: str) -> str:
    """Subscribes a customer to the SNS topic for their station.
    Returns the subscription ARN."""

    sns_client = get_sns_client()

    subscription_arns = [subscription["SubscriptionArn"] for subscription in sns_client.list_subscriptions_by_topic(
        TopicArn=get_sns_topic_arn())["Subscriptions"] if subscription["Endpoint"] == user_email]

    if len(subscription_arns) == 0:
        return sns_client.subscribe(
            TopicArn=get_sns_topic_arn(),
            Protocol="email",
            Endpoint=user_email,
            Attributes={
                "FilterPolicy": dumps({
                    "stations": [
                        station_name
                    ]
                })
            },
            ReturnSubscriptionArn=True
        )

    current_filter_policy = loads(sns_client.get_subscription_attributes(
        SubscriptionArn=subscription_arns[0])["Attributes"]["FilterPolicy"])

    current_filter_policy["stations"].append(station_name)

    sns_client.set_subscription_attributes(
        SubscriptionArn=subscription_arns[0],
        AttributeName="FilterPolicy",
        AttributeValue=dumps(current_filter_policy)
    )

    return subscription_arns[0]


def save_subscription(user_email: str, station_id: int, subscription_type: str = "station", station_name: str = None) -> bool:
    try:
        customer_id = get_or_create_customer_id(user_email)
        run_change(
            """
            INSERT INTO subscription (customer_id, station_id, subscription_type)
            VALUES (%s, %s, %s);
            """,
            values=(customer_id, int(station_id), subscription_type),
        )

        if subscription_type == "station" and station_name:
            subscribe_customer(user_email, station_name)

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
        station_name = chosen_row.iloc[0]["station_name"]

        station_ok = save_subscription(
            email,
            station_id,
            subscription_type="station",
            station_name=station_name
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


if __name__ == "__main__":
    load_dotenv()

    print(subscribe_customer(
        "trainee.sufyan.shah@sigmalabs.co.uk", "Sidcup"))
