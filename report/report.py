"""Script for generating a single PDF report on the past 24 hours of data
and sending emails with the attached report."""

from os import environ as ENV, _Environ, remove, listdir
from json import loads, dumps
from datetime import datetime
from re import match
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from logging import getLogger, basicConfig, INFO

from dotenv import load_dotenv
from xhtml2pdf import pisa
import boto3

logger = getLogger(__name__)
basicConfig(level=INFO)

LOGO_SRC = "../logo/default.png"
TODAY = datetime.today()


def generate_report_filename() -> str:
    """Returns a filename for the report depending on the current date."""

    today = datetime.strftime(TODAY, "%Y-%m-%d")

    return f"{today}-summary-report-national-rail.pdf"


def convert_html_to_pdf(source_html: str, output_filename: str) -> None:
    """Converts a HTML template to PDF and saves it under the specified name.
    Returns whether the conversion and saving was successful."""

    result_file = open(output_filename, "w+b")

    pisa.CreatePDF(
        source_html,
        dest=result_file)

    result_file.close()


def create_report(source_html: str) -> None:
    """Saves a PDF summary report, appending the source HTML into the PDF."""

    today = datetime.strftime(TODAY, "%Y/%m/%d")

    template = f'''
    <div>
        <img width=100 height=100 align="right" src="{LOGO_SRC}">
        <h1 align="center" style="font-size: 30px">{today} - Summary Report for National Rail</h1>
    </div>
    ''' + source_html

    convert_html_to_pdf(template, generate_report_filename())

    logger.info("Saved PDF summary report from HTML source.")


def delete_pdf_reports() -> None:
    """Deletes all PDF files in the current directory."""

    all_files = listdir('.')

    for file in all_files:
        if match(r".*\.pdf", file):
            remove(file)


def send_email(config: _Environ, destination_emails: list[str]) -> None:
    """Sends an email attaching a PDF summary report to the destination emails.
    SOURCE_EMAIL must exist in the config."""

    client = boto3.client("ses",
                          region_name=config["AWS_REGION"],
                          aws_access_key_id=config["AWS_ACCESS_KEY"],
                          aws_secret_access_key=config["AWS_SECRET_KEY"])
    message = MIMEMultipart()

    today = datetime.strftime(TODAY, "%d/%m/%Y")

    message["Subject"] = f"Daily Summary Report for National Rail - {today}"

    report_filename = generate_report_filename()

    attachment = MIMEApplication(open(report_filename, "rb").read())
    attachment.add_header("Content-Disposition",
                          "attachment", filename=report_filename)
    message.attach(attachment)

    text = f"""
    Attached is a PDF summary report of National Rail train data on {today}. This includes historical analysis and incident data.
    
    Kind regards,

    Signal Shift Team"""

    message.attach(MIMEText(text))

    client.send_raw_email(
        Source=config["SOURCE_EMAIL"],
        Destinations=destination_emails,
        RawMessage={
            'Data': message.as_string()
        }
    )

    logger.info("Sent email to destination emails.")


def handler(event=None, context=None):
    """Lambda function handler for generating PDF reports.
    Event expects a JSON-formatted string of all destination emails to send the report to."""

    load_dotenv()

    # Insert source HTML for report data via another script
    create_report("")

    send_email(ENV, loads(event)["destination_emails"])

    delete_pdf_reports()


if __name__ == "__main__":

    load_dotenv()

    your_email = input("Enter your email: ")

    handler(event=dumps({"destination_emails": [your_email]}))
