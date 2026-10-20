"""Implement station data and search functions in this file."""


import json
    
def get_all_stations():
    
    stations = json.loads(open("data/stations.json").read())
    return stations


import stations
from stations import get_all_stations
def get_station(code):
    stations = json.loads(open("data/stations.json").read())
    


def get_station(code):
    stations = json.loads(open("data/stations.json").read())
    
    for station in stations:
        if station["code"] == code:
        
            return station
       
    return None
    