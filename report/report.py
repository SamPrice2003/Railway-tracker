"""Script for generating a PDF report on the past 24 hours of data."""

from fpdf import FPDF


def handler(event=None, context=None):
    """Lambda function handler for generating PDF reports."""

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.image("../logo/", x=20, y=60)

    pdf.output("output.pdf")

    print("PDF generated successfully!")


if __name__ == "__main__":
    handler()
