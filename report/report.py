"""Script for generating a single PDF report on the past 24 hours of data."""

from os import environ as ENV, _Environ
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from dotenv import load_dotenv
from xhtml2pdf import pisa
import boto3

LOGO_SRC = "../logo/default.png"


def generate_report_filename() -> str:
    """Returns a filename for the report depending on the current date."""

    today = datetime.strftime(datetime.today(), "%Y-%m-%d")

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

    today = datetime.strftime(datetime.today(), "%Y/%m/%d")

    template = f'''
    <div>
        <img width=100 height=100 align="right" src="{LOGO_SRC}">
        <h1 align="center" style="font-size: 30px">{today} - Summary Report for National Rail</h1>
    </div>
    ''' + source_html

    convert_html_to_pdf(template, generate_report_filename())


def send_email(config: _Environ):

    client = boto3.client("ses",
                          region_name=config["AWS_REGION"],
                          aws_access_key_id=config["AWS_ACCESS_KEY"],
                          aws_secret_access_key=config["AWS_SECRET_KEY"])
    message = MIMEMultipart()
    message["Subject"] = "Local Test"

    report_filename = generate_report_filename()

    attachment = MIMEApplication(open(report_filename, "rb").read())
    attachment.add_header("Content-Disposition",
                          "attachment", filename=report_filename)
    message.attach(attachment)

    print(message)

    client.send_raw_email(
        Source="sl-coaches@proton.me",
        Destinations=[
            "trainee.omar.yahya@sigmalabs.co.uk",
        ],
        RawMessage={
            'Data': message.as_string()
        }
    )


def handler(event=None, context=None):
    """Lambda function handler for generating PDF reports."""

    load_dotenv()

    create_report("")

    send_email(ENV)


if __name__ == "__main__":

    load_dotenv()

    handler()
