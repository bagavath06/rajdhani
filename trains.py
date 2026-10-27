"""Implement train search functions in this file."""
"""Implement train search functions in this file."""
import json
def get_all_trains():
    
    trains = json.loads(open("data/trains.json").read())
    return trains

def get_train(number):

    trains = json.loads(open("data/trains.json").read())
    for train in trains:
        if train["number"] == number:
            return train
    return None

def get_schedule(number):
    schedules = json.loads(open(f"data/schedules/{number}.json").read())
    for schedule in schedules:
        if schedule["train_number"] == number:
            return schedules
    else:
        return None

def search_trains(
    from_station_code,
    to_station_code,
    ticket_class=None,
    departure_date=None,
    departure_time=[],
    arrival_time=[]):
    
    match_trains = [train for train in get_all_trains() if ( ticket_class in train["ticket_classes"] or ticket_class == None) and (from_station_code == train["from_station_code"] and   to_station_code ==  train["to_station_code"])]
    return match_trains


def departure(trains):
    return trains["departure"]

def arrival(trains):
    return trains["arrival"]

def duration(trains):
    total = int(trains["duration_h"]) + (int(trains["duration_m"])/60)
    return total
    
def sort_trains(trains, by, reverse = False):
    return sorted(trains, key = by, reverse = reverse)

    

