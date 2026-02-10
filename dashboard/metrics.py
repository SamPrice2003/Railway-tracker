"""Helpers for loading arrival data and calculating dashboard KPI numbers."""

import pandas as pd

from database_connection import fetch_dataframe


def load_arrivals(lookback_days: int = 7) -> pd.DataFrame:
    """Load arrivals from the database for the last N days."""
    days = int(lookback_days)

    sql = """
        SELECT
            a.arrival_station_id,
            a.arrival_date,
            a.scheduled_time,
            a.actual_time,
            a.location_cancelled,
            a.service_id,
            o.operator_name
        FROM arrival AS a
        LEFT JOIN service AS s
            ON a.service_id = s.service_id
        LEFT JOIN operator AS o
            ON s.operator_id = o.operator_id
        WHERE a.arrival_date >= CURRENT_DATE - (%s || ' days')::interval;
    """

    return fetch_dataframe(sql, values=(days,))


def get_kpi_numbers(arrivals_df: pd.DataFrame, delay_limit_mins: int = 5) -> dict:
    """Work out cancellation and delay KPI numbers from the arrivals data."""
    if arrivals_df is None or arrivals_df.empty:
        return {
            "cancellation_rate": 0.0,
            "delay_rate": 0.0,
            "avg_delay_all": 0.0,
            "avg_delay_delayed": 0.0,
        }

    data = arrivals_df.copy()

    cancelled_mask = _get_cancelled_mask(data)
    cancellation_rate = float(cancelled_mask.mean())

    delays = _get_delay_minutes(data, cancelled_mask)
    if delays.empty:
        return {
            "cancellation_rate": cancellation_rate,
            "delay_rate": 0.0,
            "avg_delay_all": 0.0,
            "avg_delay_delayed": 0.0,
        }

    limit = int(delay_limit_mins)
    delayed_mask = delays >= limit

    delay_rate = float(delayed_mask.mean())
    avg_delay_all = float(delays.mean())
    avg_delay_delayed = float(
        delays[delayed_mask].mean()) if delayed_mask.any() else 0.0

    return {
        "cancellation_rate": cancellation_rate,
        "delay_rate": delay_rate,
        "avg_delay_all": avg_delay_all,
        "avg_delay_delayed": avg_delay_delayed,
    }


def _get_cancelled_mask(data: pd.DataFrame) -> pd.Series:
    """Return a boolean mask for cancelled rows based on location_cancelled."""
    if "location_cancelled" not in data.columns:
        return pd.Series(False, index=data.index)

    return data["location_cancelled"].fillna(False).astype(bool)


def _get_delay_minutes(data: pd.DataFrame, cancelled_mask: pd.Series) -> pd.Series:
    """Return delay minutes for non cancelled rows and treat early trains as zero."""
    needed_cols = {"arrival_date", "scheduled_time", "actual_time"}
    if not needed_cols.issubset(set(data.columns)):
        return pd.Series(dtype="float64")

    base_date = pd.to_datetime(
        data["arrival_date"].astype(str), errors="coerce")

    scheduled_time = pd.to_timedelta(
        data["scheduled_time"].astype(str), errors="coerce")
    actual_time = pd.to_timedelta(
        data["actual_time"].astype(str), errors="coerce")

    scheduled_dt = base_date + scheduled_time
    actual_dt = base_date + actual_time

    good_rows = (~cancelled_mask) & scheduled_dt.notna() & actual_dt.notna()
    if good_rows.sum() == 0:
        return pd.Series(dtype="float64")

    delays = (actual_dt[good_rows] - scheduled_dt[good_rows]
              ).dt.total_seconds() / 60.0
    return delays.clip(lower=0)
