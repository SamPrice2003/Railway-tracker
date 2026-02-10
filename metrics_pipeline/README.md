# Metrics Pipeline

## Overview

<!--insert overview here-->


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

RTT_USER=<your_RRT_API_username>
RTT_PASSWORD=<your_RRT_API_password>

AWS_ACCOUNT_ID=<your_aws_account_id>
AWS_REGION=<your_aws_region>
AWS_ECR_REPO=<your_aws_ecr_repo_name>
```


## Quick Start

To run the pipeline for today's today at the current time, run the following commands:
1. `cd metrics_pipeline`
2. `pip3 install -r requirements.txt`
3. `python3 load.py`

## Development

This section is for specific use of each script in the pipeline. 

### Extract

Running this script will return a dictionary with 2 keys - 'services' and 'arrivals'. These sub dictionaries contain all the data for services and arrivals to be uploaded later.

Run:

```sh
python3 extract.py
```

### Transform

Running this script will transform the data from dictionaries into dataframes for usage in the loading script.

Run:

```sh
python3 transform.py
```

### Load

Running this script will load all of the transformed data into the database provided with the .env credentials.

Run:


```sh
python3 load.py
```

## Pipeline

Running this script will execute the pipeline in a similar way to `load.py`. This script is formatted for a Lambda function for later use on AWS.

Run:

```sh
python3 pipeline.py
```

## Additional Information
This script is designed to be pushed to the cloud as a docker image. To do so, you need the following:
- Valid AWS credentials.
- An ECR repository and it's name.
- Docker desktop running in the background.

Once these requirements are met, with the proper environment variables set, run `bash dockerise.sh` to push the contents of the pipeline to the ECR repository. Eventually the image pushed here is to be targeted by a Lambda function, which executes every hour.
