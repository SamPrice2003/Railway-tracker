- Relevant info for the database:

  - STATION
  - station id (generated always as identity)
  - station name (get from the station name dictionary we have)
  - station crs (get from the list we make)


  - ARRIVAL
  - scheduled arrival time (from the gbttbookedarrival)
  - actual arrival time (from the realtimearrival)
  - platform changed (from platform changed)
  - arrival station id (this may need to be matched up by accessing the RDS with the stations in and getting the id for the station if it's in there/ If not put it in and use that as the id)
  - service id (this most likely comes from the database too when we have the services we know about with ids referring to each service uid)

  
  - SERVICE
  - service uid (from the service uid list)
  - origin station id (when we collect the data on the services, we can collect the name. This is matched with a station in the database to get the id)
  - destination station id (when we collect the data on the services, we can collect the name. This is matched with a station in the database to get the id)


  
