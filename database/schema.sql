-- Schema for the PostgreSQL database on AWS RDS.

DROP TABLE IF EXISTS service_assignment CASCADE;
DROP TABLE IF EXISTS incident CASCADE;
DROP TABLE IF EXISTS arrival CASCADE;
DROP TABLE IF EXISTS service CASCADE;
DROP TABLE IF EXISTS operator CASCADE;
DROP TABLE IF EXISTS station CASCADE;
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS subscription CASCADE;


CREATE TABLE IF NOT EXISTS station (
    station_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    station_name VARCHAR NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    station_crs VARCHAR UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS operator (
    operator_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    operator_name VARCHAR UNIQUE NOT NULL,
    url VARCHAR
);

CREATE TABLE IF NOT EXISTS service (
    service_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    service_uid VARCHAR(6) UNIQUE NOT NULL,
    origin_station_id INT,
    destination_station_id INT,
    operator_id INT,
    FOREIGN KEY (origin_station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (destination_station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (operator_id) REFERENCES operator(operator_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS arrival (
    arrival_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    arrival_date DATE,
    scheduled_time TIME,
    actual_time TIME,
    platform_changed BOOLEAN,
    location_cancelled BOOLEAN,
    arrival_station_id INT,
    service_id INT NOT NULL,
    FOREIGN KEY (arrival_station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS incident (
    incident_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    summary TEXT,
    incident_start TIMESTAMP NOT NULL,
    incident_end TIMESTAMP,
    url VARCHAR,
    planned BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS service_assignment (
    service_assignment_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    service_id INT NOT NULL,
    incident_id INT NOT NULL,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE,
    FOREIGN KEY (incident_id) REFERENCES incident(incident_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS customer (
    customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_email VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS subscription (
    subscription_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    subscription_type VARCHAR NOT NULL CHECK (subscription_type in ('report', 'station')),
    station_id INT,
    customer_id INT NOT NULL,
    FOREIGN KEY (station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

\copy station(station_name, latitude, longitude, station_crs) from './crs.csv' WITH DELIMITER ',' CSV HEADER;
        
\copy operator (operator_name, url) from './operators.csv' WITH DELIMITER ',' CSV HEADER;

