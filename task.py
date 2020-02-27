import math
from datetime import date


def firstrun():
    return "success"


def pi():
    radius = 3
    area = float(radius**2) * float(math.pi)
    return int(area)


def list():
    thislist = ["apple", "banana", "cherry"]
    first = thislist[0]
    last = thislist[-1]
    return first, last


def time():
    today = date(2020,2,27)
    lastYear = date(2019, 2, 27)
    difference = today - lastYear
    return difference.days
