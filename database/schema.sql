-- Schema for the PostgreSQL database on AWS RDS

DROP TABLE IF EXISTS incident_assignment CASCADE;
DROP TABLE IF EXISTS incident CASCADE;
DROP TABLE IF EXISTS arrival CASCADE;
DROP TABLE IF EXISTS service CASCADE;
DROP TABLE IF EXISTS operator CASCADE;
DROP TABLE IF EXISTS station CASCADE;


CREATE TABLE station (
    station_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    station_name VARCHAR NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    station_crs VARCHAR UNIQUE NOT NULL
);

CREATE TABLE operator (
    operator_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    operator_name VARCHAR UNIQUE NOT NULL,
    url VARCHAR
);

CREATE TABLE service (
    service_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    service_uid VARCHAR(6) UNIQUE NOT NULL,
    origin_station_id INT NOT NULL,
    destination_station_id INT NOT NULL,
    operator_id INT NOT NULL,
    FOREIGN KEY (origin_station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (destination_station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (operator_id) REFERENCES operator(operator_id) ON DELETE CASCADE
);

CREATE TABLE arrival (
    arrival_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    scheduled_time TIMESTAMP,
    actual_time TIMESTAMP,
    platform_changed BOOLEAN,
    arrival_station_id INT NOT NULL,
    service_id INT NOT NULL,
    FOREIGN KEY (arrival_station_id) REFERENCES station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

CREATE TABLE incident (
    incident_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    summary TEXT,
    incident_start TIMESTAMP NOT NULL,
    incident_end TIMESTAMP,
    url VARCHAR,
    planned BOOLEAN NOT NULL,
    service_id INT NOT NULL,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

CREATE TABLE incident_assignment (
    incident_assignment_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    incident_id INT NOT NULL,
    operator_id INT NOT NULL,
    FOREIGN KEY (incident_id) REFERENCES incident(incident_id) ON DELETE CASCADE,
    FOREIGN KEY (operator_id) REFERENCES operator(operator_id) ON DELETE CASCADE
);


\copy station(station_name, latitude, longitude, station_crs) from './crs.csv' WITH DELIMITER ',' CSV HEADER;
        
\copy operator (operator_name, url) from './operators.csv' WITH DELIMITER ',' CSV HEADER;

