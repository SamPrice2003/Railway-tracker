"""Script for generating a single PDF report on the past 24 hours of data."""

from os import environ as env
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from dotenv import load_dotenv
from xhtml2pdf import pisa
import boto3

LOGO_SRC = "../logo/default.png"


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
        <h1 style="font-size: 30px">{today} - Summary Report for National Rail</h1>
    </div>
    ''' + source_html

    convert_html_to_pdf(template, "report.pdf")


def handler(event=None, context=None):
    """Lambda function handler for generating PDF reports."""

    create_report("")


if __name__ == "__main__":

    load_dotenv()

    handler()
