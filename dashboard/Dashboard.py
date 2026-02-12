"""Main Streamlit app for the Railway Tracker dashboard."""
import base64
from datetime import date, timedelta
from pathlib import Path

import streamlit as st
from streamlit_folium import st_folium

from incidents_page import render_incidents_page
from map_visualisation import (
    build_map,
    build_station_lateness,
    load_arrivals_for_day,
    load_stations,
)
from metrics import get_kpi_numbers, load_arrivals
from subscribe_page import render_subscribe_page
from unsubscribe_page import render_unsubscribe_page
from visualisations import (
    show_avg_delay_line,
    show_cancellation_donut,
    show_delay_gauge,
    show_delay_histogram,
    show_operator_delay_bars,
)

BASE_DIR = Path(__file__).resolve().parent.parent  
SIDEBAR_LOGO_PATH = BASE_DIR / "logo" / \
    "vector" / "default-monochrome-white-text.svg"
MAIN_LOGO_PATH = BASE_DIR / "logo" / "vector" / "gradient-logo.svg"


def read_svg_as_b64(file_path: Path) -> str:
    """Read an SVG file and return it as base64 text."""
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def add_css() -> None:
    """Add the CSS used to style the dashboard."""
    st.markdown(
        """
        <style>
          [data-testid="stSidebar"] {
            background: linear-gradient(
              180deg,
              #0a2540 0%,
              #1e40af 45%,
              #60a5fa 100%
            );
            border-right: none;
          }

          [data-testid="stSidebar"] * {
            color: white !important;
          }

          .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
          }

          .ss-wrapper {
            width: min(1200px, 100%);
            margin: 0 auto;
            padding: 0 1rem;
          }

          .ss-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 10px;
          }

          .ss-logo img {
            width: clamp(120px, 18vw, 180px);
            height: auto;
            display: block;
          }

          .ss-subtitle {
            text-align: center;
            font-size: 0.95rem;
            margin-top: 0.25rem;
            margin-bottom: 1.5rem;
            color: #1e40af;
          }

          .ss-caption {
            color: #2563eb !important;
            font-size: 0.85rem;
            opacity: 0.95;
            margin: 0 0 0.25rem 0;
            font-weight: 600;
          }

          div[data-testid="stMetricValue"] {
            color: #2563eb !important;
            font-weight: 700 !important;
          }

          div[data-testid="stMetricLabel"] {
            color: #111827 !important;
            font-weight: 600 !important;
          }

          .ss-nav [role="radiogroup"] label > div:first-child { display: none; }

          .ss-nav label {
            padding: 10px 14px;
            border-radius: 10px;
            margin-bottom: 6px;
            cursor: pointer;
          }

          .ss-nav label:hover {
            background: rgba(255,255,255,0.08);
          }

          .ss-nav input:checked + div {
            background: rgba(255,255,255,0.18);
            border-radius: 10px;
            font-weight: 600;
          }

          h2, h3 { color: #1e40af; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_sidebar_logo() -> None:
    """Show the logo at the top of the sidebar."""
    logo_b64 = read_svg_as_b64(SIDEBAR_LOGO_PATH)
    st.sidebar.markdown(
        f"""
        <div style="text-align:center; padding: 1rem 0 0.75rem 0;">
          <img src="data:image/svg+xml;base64,{logo_b64}"
               style="width: 140px; max-width: 80%; height: auto;" />
        </div>
        <hr style="border:none; border-top:1px solid rgba(255,255,255,0.18);
                   margin:0.5rem 0 0.75rem 0;">
        """,
        unsafe_allow_html=True,
    )


def pick_page() -> str:
    """Let the user pick which page to view and return the choice."""
    with st.sidebar:
        st.markdown("<div class='ss-nav'>", unsafe_allow_html=True)
        page_name = st.radio(
            "",
            ["Dashboard", "Incidents", "Subscribe"],
            index=0,
            key="nav_page",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    return page_name


def slogan() -> None:
    st.markdown(
        """
        <div class="ss-subtitle">
          Tracking shifts in train schedules for you.
        </div>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data(ttl=300)
def get_stations() -> object:
    """Load station data and cache it for a short time."""
    return load_stations()


@st.cache_data(ttl=300)
def get_arrivals_for_charts(days_back: int) -> object:
    """Load arrival rows for KPI and chart use and cache it for a short time."""
    return load_arrivals(previous_days=int(days_back))


@st.cache_data(ttl=300)
def get_arrivals_for_map(chosen_day: date) -> object:
    """Load arrival rows for a chosen day on the map and cache it for a short time."""
    return load_arrivals_for_day(chosen_day)


def show_dashboard() -> None:
    """Render the main dashboard page."""
    st.markdown('<div class="ss-wrapper">', unsafe_allow_html=True)
    slogan()

    st.markdown("")

    with st.spinner("Loading stations..."):
        stations_df = get_stations()

    with st.spinner("Loading KPI data..."):
        raw_kpi_rows = get_arrivals_for_charts(7)
        kpis = get_kpi_numbers(
            raw_kpi_rows, delay_limit_mins=5)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cancellation Rate", f"{kpis['cancellation_rate'] * 100:.1f}%")
    col2.metric(
        f"Delay Rate (≥ {5} mins)",
        f"{kpis['delay_rate'] * 100:.1f}%",
    )
    col3.metric("Average Delay (All Trains)",
                f"{kpis['avg_delay_all']:.1f} mins")
    col4.metric(
        "Average Delay (Delayed Trains Only)",
        f"{kpis['avg_delay_delayed']:.1f} mins",
    )

    st.divider()

    st.subheader("Service reliability (7 Days)")
    left, right = st.columns(2, gap="large")

    with left:
        st.markdown(
            "<div class='ss-caption'>Percentage of trains cancelled</div>",
            unsafe_allow_html=True,
        )
        show_cancellation_donut(
            kpis["cancellation_rate"], key="cancel_donut_main")

    with right:
        st.markdown(
            (
                "<div class='ss-caption'>Percentage of trains with severe delays "
                f"(≥ {5} mins)</div>"
            ),
            unsafe_allow_html=True,
        )
        st.markdown("<div style='margin-top: 100px;'></div>",
                    unsafe_allow_html=True)
        show_delay_gauge(kpis["delay_rate"], key="delay_gauge_main")

    st.divider()

    st.subheader("Average delay trend")
    st.markdown(
        "<div class='ss-caption'>Trend time window (days)</div>",
        unsafe_allow_html=True,
    )
    trend_days = st.slider(
    "", 
        min_value=1,
        max_value=30,
        value=7,
        step=1,
        key="trend_window_days",
    )

    with st.spinner("Loading trend data..."):
        raw_trend_rows = get_arrivals_for_charts(trend_days)

    show_avg_delay_line(
        raw_trend_rows,
        previous_days=trend_days,
        group_by="H",
        smooth_window=6,
        key="avg_delay_sparkline_main",
    )

    st.divider()

    st.subheader("Delay distribution")
    st.markdown(
        "<div class='ss-caption'>Delay distribution time window (days)</div>",
        unsafe_allow_html=True,
    )
    dist_days = st.slider(
        "",
        min_value=1,
        max_value=30,
        value=7,
        step=1,
        key="dist_window_days",
    )

    with st.spinner("Loading distribution data..."):
        raw_dist_rows = get_arrivals_for_charts(dist_days)

    show_delay_histogram(
        raw_dist_rows,
        previous_days=dist_days,
        bin_count=30,
        max_delay_mins=60,
        key="delay_histogram_main",
    )

    st.markdown("")

    st.subheader("Delay by operator")
    st.markdown(
        "<div class='ss-caption'>Operator time window (days)</div>",
        unsafe_allow_html=True,
    )
    operator_days = st.slider(
        "",
        min_value=1,
        max_value=30,
        value=7,
        step=1,
        key="op_window_days",
    )

    with st.spinner("Loading operator data..."):
        raw_operator_rows = get_arrivals_for_charts(operator_days)

    show_operator_delay_bars(
        raw_operator_rows,
        previous_days=operator_days,
        metric="Mean",
        top_n=10,
        max_delay_mins=60,
        min_services=30,
        key="avg_delay_by_operator_main",
    )

    st.divider()

    st.subheader("Station lateness map")

    today = date.today()
    earliest_day = today - timedelta(days=30)

    chosen_day = st.date_input(
        "Select a day",
        value=today,
        min_value=earliest_day,
        max_value=today,
        key="map_selected_day",
    )

    st.markdown(
        "<div class='ss-caption'>Map late threshold (mins)</div>",
        unsafe_allow_html=True,
    )


    late_limit = st.slider(
    "",
        min_value=1,
        max_value=10,
        value=2,
        step=1,
        key="map_late_threshold",
    )

    with st.spinner("Loading map data..."):
        arrivals_for_day = get_arrivals_for_map(chosen_day)

    if arrivals_for_day is None or arrivals_for_day.empty:
        st.warning("No arrivals available for this day.")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    day_rows = arrivals_for_day.copy()
    day_rows["is_late"] = day_rows["delay_minutes"] >= late_limit
    lateness_df = build_station_lateness(stations_df, day_rows)

    if lateness_df.empty:
        st.warning("No stations to display for this day.")
    else:
        folium_map = build_map(stations_df, lateness_df)
        st_folium(folium_map, use_container_width=True,
                  height=650, key="lateness_map")

    st.markdown("</div>", unsafe_allow_html=True)


def run_app() -> None:
    """Set up the app and route to the selected page."""
    st.set_page_config(
        page_title="Signal Shift",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    add_css()
    show_sidebar_logo()

    view = st.query_params.get("view")
    if view == "unsubscribe":
        render_unsubscribe_page()
        return

    page = pick_page()

    if page == "Dashboard":
        show_dashboard()
    elif page == "Incidents":
        render_incidents_page()
    else:
        render_subscribe_page()


if __name__ == "__main__":
    run_app()
