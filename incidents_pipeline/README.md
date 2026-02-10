## Incidents Feed Pipeline

This is a pipeline for retrieving incidents on National Rail lines in real time. This is then cleaned, processed, and uploaded to the RDS database to be used for the dashboard.

## Environment Variables

The `.env` file should contain the following:

```
STOMP_HOST=XXXX
STOMP_PORT=61613
STOMP_USERNAME=XXXX
STOMP_PASSWORD=XXXX
STOMP_TOPIC=XXXX
DB_HOST=XXXX
DB_PORT=XXXX
DB_NAME=XXXX
DB_USERNAME=XXXX
DB_PASSWORD=XXXX
AWS_ACCESS_KEY=XXXX
AWS_SECRET_KEY=XXXX
AWS_REGION=XXXX
AWS_ECR_REPO=XXXX
INCIDENT_TOPIC=XXXX
```

The STOMP information can be found via registering for the [National Rail Data Portal](https://opendata.nationalrail.co.uk/feeds). It is located under the title "Knowledgebase (KB) Real Time Incidents".

The `AWS_ECR_REPO` is exactly the same as the repository that you have provided for the `LISTENER_IMAGE_URI` in the Terraforming folder. This is only required if you run `dockerise.sh` as detailed in [this section](#aws-ecr).


## Quick Start

### Local Pipeline

If you would like to run the pipeline to listen for incidents and add them to the `incident` table in the database continuously, run the following:

```sh
python pipeline.py
```

### AWS ECR Imaging

If you would like to push an image of the pipeline to your ECR repository, simply run the following:

```sh
sh dockerise.sh
```

Bear in mind you must have `AWS_REGION` and `AWS_ECR_REPO` in your [environment variables](#environment-variables).


## Development

This section is for specific use of each script in the pipeline.

### Extract

Running this script will continuously print new incidents found on the incidents feed by National Rail:

```sh
python extract.py
```

### Transform

Running this script will also continuously print new incidents found on the incidents feed by National Rail:

```sh
python transform.py
```

The output data is in a cleaned and understandable format instead of raw.

### Load

Running this script will wait for a new incident from the incidents feed by National Rail and add the data to the `incident` table in our database:

```sh
python load.py
```

This script stops after a single upload is made.

### Alert

Running this script will wait for a new incident, add it to the `incident` table, then publish the incident to our `INCIDENT_TOPIC` via SNS:

```sh
python alert.py
```

This script runs continuously.