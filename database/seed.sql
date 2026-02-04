-- SQL script to seed data into the relevant tables.

\copy station (station_name, station_crs)
FROM './crs.csv'
DELIMITER ','
CSV HEADER;

\copy operator (operator_name, url)
FROM './operators.csv'
WITH DELIMITER ','
CSV HEADER;
