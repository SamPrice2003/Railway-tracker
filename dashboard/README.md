# Railway Tracker Dashboard (Streamlit)
This dashboard is the front end for the Railway Tracker project. It connects to a Postgres database to display metrics, maps, incidents, and allows users to subscribe or unsubscribe to station alerts.

## Prerequisites
- Python 3.10+ 
- Postgres database (local Postgres or AWS RDS)
- Network access to the database (security group rules if using RDS)

## Project structure
Common files in this folder:
- `dashboard.py` main Streamlit entrypoint
- `database_connection.py` database helpers using environment variables
- `subscribe_page.py` subscribe UI and DB writes
- `unsubscribe_page.py` unsubscribe UI and DB writes
- `map_visualisation.py` UK map view
- `metrics.py` metrics queries and visuals
- `incidents_page.py` incidents list and filters
- `requirements.txt` Python dependencies

## Setup

### 1. Create a virtual environment

Mac or Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your .env file

This project uses environment variables for database credentials. Create a file called .env inside the dashboard/ folder (same folder as database_connection.py).

Example:

```bash
DB_HOST=your-db-hostname
DB_PORT=5432
DB_NAME=your-db-name
DB_USERNAME=your-db-username
DB_PASSWORD=your-db-password
```

Notes:

DB_PORT defaults to 5432 if not provided.

Do not commit .env to git.
Add this to .gitignore if not already present:

```bash
.env
```

### 4. Database Schema

Ensure the database has the schema uploaded before attempting to run the dashboard. The schema can be found in the database folder and can be executed by running: 

```bash
bash run_schema.sh
```

### 5. Running the dashboard 

To run the dashboard, execute: 

```bash
streamlit run Dashboard.py
```
