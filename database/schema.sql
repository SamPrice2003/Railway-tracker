-- schema for the postgres db

-- create tables

CREATE TABLE service (
    service_id INT GENERATED ALWAYS AS IDENTITY,
    service_uid VARCHAR(6) UNIQUE NOT NULL,
    origin_station_id INT NOT NULL,
    destination_station_id INT NOT NULL
)

CREATE TABLE arrival (
    arrival_id INT GENERATED ALWAYS AS IDENTITY,
    scheduled_time TIMESTAMP,
    actual_time TIMESTAMP,
    platform_changed BOOLEAN,
    arrival_station_id INT,
    service_id INT
)

CREATE TABLE station (
    station_id INT GENERATED ALWAYS AS IDENTITY,
    station_name VARCHAR UNIQUE NOT NULL,
    station_crs VARCHAR UNIQUE NOT NULL
)

CREATE TABLE incident (
    incident_id INT GENERATED ALWAYS AS IDENTITY,
    summary TEXT
)



