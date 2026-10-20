"""Implement station data and search functions in this file."""


import json
    
def get_all_stations():

    return json.loads(open("data/stations.json").read())


def get_station(code):
    
    for station in stations:
        if station["code"] == code:
        
            return station
       
    return None
    

