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
STOMP_HOST=<your_national_rail_API_STOMP_host>
STOMP_PORT=<your_national_rail_API_STOMP_port>
STOMP_USERNAME=<your_national_rail_API_STOMP_username>
STOMP_PASSWORD=<your_national_rail_API_STOMP_password>
STOMP_TOPIC=<your_national_rail_API_STOMP_topic>
RTT_USER=<your_RRT_API_username>
RTT_PASSWORD=<your_RRT_API_password>
```


## Quick Start

<!--Insert quick start info here-->


## Development

This section is for specific use of each script in the pipeline. 

### Extract

Running this script will <!--Insert what it does-->:

```sh
python extract.py
```

### Transform

Running this script will <!--Insert what it does-->:

```sh
python transform.py
```

### Load

Running this script will <!--Insert what it does-->:

```sh
python load.py
```