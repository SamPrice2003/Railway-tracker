"""Script for generating a single PDF report on the past 24 hours of data
and sending emails with the attached report."""

from os import environ as ENV, _Environ, remove, listdir
from datetime import datetime
from re import match
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from logging import getLogger, basicConfig, INFO

from dotenv import load_dotenv
from xhtml2pdf import pisa
import boto3

from report_html import generate_report_html
from upload_to_s3 import get_s3_client, upload_to_s3
from metrics import get_db_connection

logger = getLogger(__name__)
basicConfig(level=INFO)

LOGO_SRC = "../logo/default.png"
TODAY = datetime.today()


def generate_report_filename() -> str:
    """Returns a filename for the report depending on the current date."""

    today = datetime.strftime(TODAY, "%Y-%m-%d")

    return f"{today}-summary-report-national-rail.pdf"


def convert_html_to_pdf(source_html: str, output_filename: str) -> None:
    """Converts a HTML template to PDF and saves it under the specified name."""

    with open(output_filename, "w+b") as f:
        pisa.CreatePDF(
            source_html,
            dest=f)


def create_report() -> str:
    """Saves a PDF summary report based on database metrics.
    Returns the file name of the PDF summary report saved."""

    today = datetime.strftime(TODAY, "%Y/%m/%d")

    template = f'''
    <div>
        <img width=100 height=100 align="right" src="{LOGO_SRC}">
        <h1 align="center" style="font-size: 30px">{today} - Summary Report for National Rail</h1>
    </div>
    ''' + generate_report_html()

    pdf_file = generate_report_filename()

    convert_html_to_pdf(template, pdf_file)

    logger.info("Saved PDF summary report from HTML source.")

    return pdf_file


def delete_pdf_reports() -> None:
    """Deletes all PDF files in the current directory."""

    all_files = listdir('.')

    for file in all_files:
        if match(r".*\.pdf", file):
            remove(file)


def get_destination_emails(config: _Environ) -> list[str]:
    """Returns a list of the destination emails for the PDF report."""

    with get_db_connection(config).cursor() as cur:
        cur.execute("""
                    SELECT DISTINCT customer_email
                    FROM customer
                    JOIN subscription
                        USING (customer_id)
                    WHERE subscription_type LIKE '%%report%'
                    ;
                    """)

        return [row["customer_email"] for row in cur.fetchall()]


def send_email(config: _Environ, destination_emails: list[str], pdf_file_name: str) -> None:
    """Sends an email attaching a PDF summary report to the destination emails.
    SOURCE_EMAIL must exist in the config."""

    client = boto3.client("ses",
                          region_name=config["AWS_REGION"],
                          aws_access_key_id=config["AWS_ACCESS_KEY"],
                          aws_secret_access_key=config["AWS_SECRET_KEY"])
    message = MIMEMultipart()

    today = datetime.strftime(TODAY, "%d/%m/%Y")

    message["Subject"] = f"Daily Summary Report for National Rail - {today}"

    attachment = MIMEApplication(open(pdf_file_name, "rb").read())
    attachment.add_header("Content-Disposition",
                          "attachment", filename=pdf_file_name)
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

    pdf_file = create_report()

    dest_emails = get_destination_emails(ENV)

    send_email(ENV, dest_emails, pdf_file)

    upload_to_s3(get_s3_client(ENV), pdf_file, ENV["S3_BUCKET_NAME"], pdf_file)

    delete_pdf_reports()


if __name__ == "__main__":

    load_dotenv()

    handler()
