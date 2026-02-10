"""Script for generating the HTML contents report for the PDF using metrics.py."""

# pylint: disable=line-too-long

from os import environ as ENV

from dotenv import load_dotenv

import metrics

load_dotenv()

conn = metrics.get_db_connection(ENV)


def generate_report_html() -> str:
    """Returns the HTML content for the report with key metrics and tables."""

    total_delayed_services = metrics.get_total_delayed_services(conn)
    total_delayed_arrivals = metrics.get_total_delayed_arrivals(conn, 1)
    most_delayed_service = metrics.get_most_delayed_service(conn)
    most_delayed_lines = metrics.get_most_delayed_lines(conn)
    most_delayed_stations = metrics.get_most_delayed_stations(conn)

    return f"""
<h2 style="font-size:21px;">1. Overall Metrics</h2>

<table width="100%" cellspacing="0" cellpadding="6" border="1">
    <tr style="background-color:lightgrey">
        <th align="left">Service Metrics</th>
        <th align="right">Amount</th>
    </tr>
    <tr>
        <td>Total Scheduled Services</td>
        <td align="right">{metrics.get_total_services(conn)}</td>
    <tr>
        <td>Delayed Services</td>
        <td align="right">{total_delayed_services}</td>
    <tr>
        <td>Cancelled Services</td>
        <td align="right">{metrics.get_total_cancelled_services(conn)}</td>
    </tr>
</table>

<br>

<h2 style="font-size:21px;">2. Delay Overview</h2>

<p>The average delay across all trains was {metrics.get_average_delay(conn):.2f} minutes.

<table width="100%" cellspacing="0" cellpadding="6" border="1">
    <tr style="background-color:lightgrey">
        <th align="left">Delay Band</th>
        <th align="right">Frequency</th>
        <th align="right">% of Delayed</th>
    </tr>
    <tr>
        <td>1-5 minutes</td>
        <td align="right">{metrics.get_total_delayed_arrivals(conn, 1, 5)}</td>
        <td align="right">{(metrics.get_total_delayed_arrivals(conn, 1, 5)/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
    <tr>
        <td>6-15 minutes</td>
        <td align="right">{metrics.get_total_delayed_arrivals(conn, 6, 15)}</td>
        <td align="right">{(metrics.get_total_delayed_arrivals(conn, 6, 15)/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
    <tr>
        <td>16-30 minutes</td>
        <td align="right">{metrics.get_total_delayed_arrivals(conn, 16, 30)}</td>
        <td align="right">{(metrics.get_total_delayed_arrivals(conn, 16, 30)/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
    <tr>
        <td>30+ minutes</td>
        <td align="right">{metrics.get_total_delayed_arrivals(conn, 30)}</td>
        <td align="right">{(metrics.get_total_delayed_arrivals(conn, 30)/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
</table>

<p>The most delayed service was between {most_delayed_service["origin_station_name"]} and {most_delayed_service["destination_station_name"]},
arriving at {most_delayed_service["arrival_station_name"]} with a delay of {most_delayed_service["delay_mins"]} minutes.</p>

<table width="100%" cellspacing="0" cellpadding="6" border="1">
    <tr style="background-color:lightgrey">
        <th align="left">Time Period</th>
        <th align="right">Delay %</th>
    </tr>
    <tr>
        <td>Morning Peak (06:00-09:30)</td>
        <td align="right">{(metrics.get_total_delayed_services_between_times(conn, "06:00", "09:30")/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
    <tr>
        <td>Midday (09:30-15:30)</td>
        <td align="right">{(metrics.get_total_delayed_services_between_times(conn, "09:30", "15:30")/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
    <tr>
        <td>Evening Peak (15:30-18:30)</td>
        <td align="right">{(metrics.get_total_delayed_services_between_times(conn, "15:30", "18:30")/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
    <tr>
        <td>Off-Peak / Late</td>
        <td align="right">{((metrics.get_total_delayed_services_between_times(conn, "00:00", "06:00")
                            + metrics.get_total_delayed_services_between_times(conn, "18:30", "23:59"))/total_delayed_arrivals)*100:.2f}%</td>
    </tr>
</table>

<h2 style="font-size:21px;">3. Worst Affected Lines / Stations</h2>

<h3 style="font-size:18px;">3.1 Lines</h3>

<ul>
    <li><b>{most_delayed_lines[0]["operator_name"]}</b> - {most_delayed_lines[0]["total_delay_mins"]} total minutes delayed</li>
    <li><b>{most_delayed_lines[1]["operator_name"]}</b> - {most_delayed_lines[1]["total_delay_mins"]} total minutes delayed</li>
    <li><b>{most_delayed_lines[2]["operator_name"]}</b> - {most_delayed_lines[2]["total_delay_mins"]} total minutes delayed</li>
</ul>

<h3 style="font-size:18px;">3.2 Stations</h3>

<ul>
    <li><b>{most_delayed_stations[0]["station_name"]}</b> - {most_delayed_stations[0]["total_delay_mins"]} delayed services</li>
    <li><b>{most_delayed_stations[1]["station_name"]}</b> - {most_delayed_stations[1]["total_delay_mins"]} delayed services</li>
    <li><b>{most_delayed_stations[2]["station_name"]}</b> - {most_delayed_stations[2]["total_delay_mins"]} delayed services</li>
</ul>
"""


if __name__ == "__main__":

    with open("report.html", "w") as f:
        f.write(generate_report_html())
