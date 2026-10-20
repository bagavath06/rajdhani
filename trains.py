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
    import json
def get_schedule(number):
    schedules = json.loads(open("data/schedules/number.json").read())
    for schedule in schedules:
        if schedule["train_number"] == number:
        return schedules
    else:
        return None
