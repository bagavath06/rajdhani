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