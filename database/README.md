# Database Information

## Setup / Operation

To create the schema and seed the database, simply do the following steps:

1. Run `cd database` to move into the database directory.
2. Run `touch .env` to create the environment variables folder.
3. Populate this folder with these environment variables of the form:
```
DB_HOST= <rds_host_link>
DB_PORT= 5432
DB_NAME= <database_name>
DB_USERNAME= <your_database_username>
DB_PASSWORD= <your_database_password>
```
4. Finally, run `bash run_schema.sh` to create the schema and seed the data.

## Description of files

- `crs.csv` : The csv file containing the information about the station names and their crs codes, used to seed the *station* table in the database.
- `operators.csv` : The csv file containing the information about the operator names with a url for each one with more information.
- `run_schema.sh` : The bash script which accesses the .env file and runs the schema script with the credentials provided.
- `schema.sql` : The sql file which describes the tables in the database and seeds 2 of them with initial data.
- `Signal-Shift-ERD.png` : The entity relationship diagram showing how each of the tables in the database link together.