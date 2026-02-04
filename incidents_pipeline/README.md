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
```

The STOMP information can be found via registering for the [National Rail Data Portal](https://opendata.nationalrail.co.uk/feeds). It is located under the title "Knowledgebase (KB) Real Time Incidents".