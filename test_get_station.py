
from getstation import get_station

def test_get_station():
    assert get_station("SBC") == {'code': 'SBC',
 'name': 'BANGALORE CITY JN',
 'zone': 'SWR',
 'state': 'Karnataka',
 'address': 'Bengaluru, Karnataka',
 'latitude': 12.977595,
 'longitude': 77.56808299999999}



