"""Charts and small data prep helpers for the Streamlit dashboard."""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def keep_between_zero_and_one(rate: float ) -> float:
    """Keep a rate value between 0 and 1."""
    if rate is None:
        return 0.0
    return max(0.0, min(1.0, float(rate)))


def make_delay_table(arrivals: pd.DataFrame) -> pd.DataFrame:
    """Turn raw arrival rows into a table with delay minutes and timestamps."""
    if arrivals is None or arrivals.empty:
        return pd.DataFrame()

    table = arrivals.copy()

    if "location_cancelled" in table.columns:
        is_cancelled = table["location_cancelled"].fillna(False).astype(bool)
    else:
        is_cancelled = pd.Series(False, index=table.index)

    needed_cols = {"arrival_date", "scheduled_time", "actual_time"}
    missing_cols = needed_cols - set(table.columns)
    if missing_cols:
        st.warning(
            f"Missing columns needed for delay charts: {sorted(missing_cols)}")
        return pd.DataFrame()

    day = pd.to_datetime(table["arrival_date"].astype(str), errors="coerce")
    scheduled = pd.to_timedelta(
        table["scheduled_time"].astype(str), errors="coerce")
    actual = pd.to_timedelta(table["actual_time"].astype(str), errors="coerce")

    scheduled_time = day + scheduled
    actual_time = day + actual

    ok_rows = (~is_cancelled) & day.notna(
    ) & scheduled.notna() & actual.notna()
    table = table.loc[ok_rows].copy()
    if table.empty:
        return pd.DataFrame()

    table["scheduled_dt"] = scheduled_time.loc[ok_rows]
    table["actual_dt"] = actual_time.loc[ok_rows]

    delay_mins = (table["actual_dt"] - table["scheduled_dt"]
                  ).dt.total_seconds() / 60.0
    table["delay_minutes"] = delay_mins.clip(lower=0)

    return table


def get_recent_arrivals(arrivals: pd.DataFrame, previous_days: int) -> pd.DataFrame:
    """Return only the last N days of arrivals with delay minutes calculated."""
    table = make_delay_table(arrivals)
    if table.empty:
        return pd.DataFrame()

    latest_time = table["actual_dt"].max()
    start_time = latest_time - pd.Timedelta(days=int(previous_days))
    return table[table["actual_dt"] >= start_time].copy()


def show_cancellation_donut(cancel_rate: float, key: str = "cancel_donut") -> None:
    """Show a donut chart of cancelled vs not cancelled trains."""
    cancelled = keep_between_zero_and_one(cancel_rate)
    not_cancelled = 1.0 - cancelled

    chart = go.Figure(
        data=[
            go.Pie(
                labels=["Cancelled", "Not cancelled"],
                values=[cancelled, not_cancelled],
                hole=0.65,
            )
        ]
    )
    chart.update_layout(margin=dict(l=10, r=10, t=10, b=10), showlegend=True)
    st.plotly_chart(chart, use_container_width=True, key=key)


def show_delay_gauge(delay_rate: float, key: str = "delay_gauge") -> None:
    """Show a gauge for the percentage of delayed trains."""
    percent = keep_between_zero_and_one(delay_rate) * 100.0

    chart = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=percent,
            number={"suffix": "%"},
            gauge={
                "shape": "bullet",
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
            },
        )
    )

    chart.update_layout(height=200, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(chart, use_container_width=True, key=key)


def show_avg_delay_line(arrivals: pd.DataFrame, previous_days: int = 7, group_by: str = "H",
    smooth_window: int = 6,
    key: str = "avg_delay_sparkline",) -> None:
    """Show a smoothed line of average delay over time."""
    table = get_recent_arrivals(arrivals, previous_days)
    if table.empty:
        st.info("Not enough non cancelled records to plot average delay over time.")
        return

    table["time_bucket"] = table["actual_dt"].dt.floor(group_by)

    grouped = (
        table.groupby("time_bucket", as_index=False)
        .agg(avg_delay=("delay_minutes", "mean"))
        .sort_values("time_bucket")
    )
    grouped["avg_delay_smooth"] = grouped["avg_delay"].rolling(
        window=smooth_window,
        min_periods=1,
    ).mean()

    avg_delay = float(grouped["avg_delay"].mean()
                      ) if not grouped.empty else 0.0

    left_col, right_col = st.columns([1.3, 3.7], vertical_alignment="center")
    with left_col:
        st.metric("Average delay", f"{avg_delay:.1f} mins")

    with right_col:
        chart = go.Figure()
        chart.add_trace(
            go.Scatter(
                x=grouped["time_bucket"],
                y=grouped["avg_delay_smooth"],
                mode="lines",
                name="Average delay",
            )
        )
        chart.update_layout(
            height=170,
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=False,
            xaxis=dict(
                title=None,
                showgrid=False,
                zeroline=False,
                tickformat="%d %b\n%H:%M",
                ticks="outside",
            ),
            yaxis=dict(
                title="mins",
                showgrid=False,
                zeroline=False,
                rangemode="tozero",
            ),
        )
        st.plotly_chart(chart, use_container_width=True, key=key)


def show_delay_histogram(
    arrivals: pd.DataFrame,
    previous_days: int = 7,
    bin_count: int = 30,
    max_delay_mins: int = 60,
    key: str = "delay_histogram",
) -> None:
    """Show a histogram of delay minutes for the selected time window."""
    table = get_recent_arrivals(arrivals, previous_days)
    if table.empty:
        st.info("Not enough non cancelled records to plot delay distribution.")
        return

    table["delay_minutes"] = table["delay_minutes"].clip(
        upper=float(max_delay_mins))

    chart = go.Figure()
    chart.add_trace(
        go.Histogram(
            x=table["delay_minutes"],
            nbinsx=int(bin_count),
            name="Delays",
        )
    )
    chart.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
        xaxis=dict(title="Delay (minutes)", zeroline=False),
        yaxis=dict(title="Number of trains", zeroline=False),
        bargap=0.08,
    )
    st.plotly_chart(chart, use_container_width=True, key=key)


def show_operator_delay_bars(
    arrivals: pd.DataFrame,
    previous_days: int = 7,
    metric: str = "Mean",
    top_n: int = 10,
    max_delay_mins: int = 60,
    min_services: int = 30,
    key: str = "avg_delay_by_operator",
) -> None:
    """Show a bar chart of average or median delay by operator."""
    table = get_recent_arrivals(arrivals, previous_days)
    if table.empty:
        st.info("Not enough non cancelled records to compare operators.")
        return

    if "operator_name" not in table.columns:
        st.warning("Missing column for operator chart: operator_name")
        return

    table["delay_minutes"] = table["delay_minutes"].clip(
        upper=float(max_delay_mins))

    counts = table["operator_name"].value_counts()
    operators_to_keep = counts[counts >= int(min_services)].index
    table = table[table["operator_name"].isin(operators_to_keep)].copy()

    if table.empty:
        message = (
            f"No operators have at least {min_services} services "
            f"in the last {previous_days} days."
        )
        st.info(message)
        return

    metric_text = (metric or "Mean").strip().lower()
    use_median = metric_text.startswith("med")
    agg_name = "median" if use_median else "mean"
    label = "Median delay" if use_median else "Average delay"

    summary = (
        table.groupby("operator_name", as_index=False)
        .agg(delay=("delay_minutes", agg_name), services=("delay_minutes", "size"))
        .sort_values("delay", ascending=False)
        .head(int(top_n))
        .sort_values("delay", ascending=True)
    )

    chart = go.Figure(
        go.Bar(
            x=summary["delay"],
            y=summary["operator_name"],
            orientation="h",
            text=summary["services"].map(lambda n: f"n={n}"),
            textposition="outside",
            marker_line_width=0,
        )
    )
    chart.update_layout(
        height=max(320, 42 * len(summary)),
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
        xaxis=dict(title=f"{label} (mins)",
                   rangemode="tozero", zeroline=False),
        yaxis=dict(title=None),
        bargap=0.35,
    )
    st.plotly_chart(chart, use_container_width=True, key=key)
