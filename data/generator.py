"""
todo:
create a random (but sensible) data generator:
*should generate a number of health centers and generate randomized locations,
random staff counts, carrying capitities, etc
"""
import numpy as np
import random as rn
from faker import Faker #run 'pip install faker' first

def generate_Random_LatLong_Within_RectArea(count,long_range,lat_range):
    """
    @purpose: generates a set of coordinates bounded by four bounding box coords
    @params: 
    count: number of coordinates to generate
    long_range: 
    """
    y1,y2 = lat_range
    x1,x2 = long_range
    #[lat,long]
    return np.array([[rn.uniform(y1,y2),rn.uniform(x1,x2)] for i in range(count)])


items = ["masks","ventilators","testing kits"]
def randomRequestGenerator(items):
    """
    @purpose: generates random request objects 
    @param: a list of requested items
    @return: a dictionary of items and their (randomly generated) requested quantities
    """
    from collections import Counter
    res = Counter()
    for item in items:
        res[item] += rn.randrange(50,100)
    return dict(res)

def randomInventoryGenerator(items):
    """
    generates a list of inventory items based on item names
    """
    return [
        {'name': item,'unit_price': rn.randrange(100,200),'quantity':rn.randrange(50,100)} for item in items
    ]


def getRandomFacilityName():
    fake = Faker()
    return fake.name() + ' memorial hospital'

def randomFacilitiesGenerator(count,long_range,lat_range):
    """
    generates random facility information
    """
    from math import floor,ceil
    coords = generate_Random_LatLong_Within_RectArea(count,long_range,lat_range)
    carrying_capacities = [rn.randrange(50,200) for i in range(count)]
    return [
        {
            'name': getRandomFacilityName(),
            'location': coords[i],
            'requests': randomRequestGenerator(items),
            'carrying_capacity': carrying_capacities[i],
            'covid_testing_available': rn.choice([True,False]),
            'type': rn.choice(["hospital","clinic","pharmacy"]),
            'covid_patient_count': rn.randrange(floor(0.2*carrying_capacities[i]),floor(0.8*carrying_capacities[i]))
        }
        for i in range(count)
    ]
