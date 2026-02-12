# PDF Summary Report

## Overview

This is a set of scripts which generates a report showcasing today's National Rail metrics in a PDF format. It also emails subscribers this report and uploads the report to the S3 bucket.


## Installation & Setup

Ensure you are in the `/metrics_pipeline` directory.

1. Create a virtual environment with `python -m venv .venv`
2. Activate your venv with `source .venv/bin/activate`
3. Install required libraries via `pip install -r requirements.txt`
4. Create a file `.env` and continue with [the next section](#environment-variables).


## Environment Variables

Insert the relevant data in your `.env` file as follows:

```
DB_HOST=<your_RDS_instance_address>
DB_PORT=5432
DB_NAME=<your_database_name>
DB_USER=<your_database_username>
DB_PASSWORD=<your_database_password>
AWS_REGION=<your_aws_region>
ACCESS_KEY_AWS=<your_AWS_access_key>
SECRET_KEY_AWS=<your_AWS_secret_key>
S3_BUCKET_NAME=<your_S3_bucket_name>
AWS_ECR_REPO=<your_aws_ECR_repo_name>
SOURCE_EMAIL=<your_source_email_for_reports>
```


## Quick Start

### Local Pipeline

If you would like to send a PDF summary report email to subscribed users (in the database `subscription` table) and upload the PDF to your S3 bucket, run the following:

```sh
python report.py
```

### AWS ECR Imaging

If you would like to push an image of the pipeline to your ECR repository, simply run the following:

```sh
sh dockerise.sh
```

Bear in mind you must have `AWS_REGION` and `AWS_ECR_REPO` in your [environment variables](#environment-variables).


## Development

This section is for specific use of other scripts in the pipeline.

### Report HTML

Running this script will write a new HTML file to the current directory with the PDF report contents:

```sh
python report_html.py
```