source .env

PGPASSWORD=${DB_PASSWORD} psql ${DB_NAME} -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USERNAME} -f schema.sql


