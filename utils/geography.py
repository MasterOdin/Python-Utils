"""
A collection of useful functions I've needed for variety of projects and applications.
"""
from math import atan2, cos, sin, radians, sqrt

EARTH_RADIUS_METERS = 6373
EARTH_RADIUS_MILES = 3959


def haversine(point1, point2, miles=False):
    """
    Calculate the great-circle distance of two points using haversine formula

    Given the longtitude and latitude of two places, calculate the great-circle distance between these
    two points on a sphere. This method is not fully accurate for the earth due to its slightly
    ellipsoidal shape, resulting in errors that are generally below 0.3% (though around 0.55% error
    if the two points are on the equator of the earth)

    :param point1: Tuple containing (Latitude, Longtitude) of the first point
    :param point2: Tuple containing (Latitude, Longtitude) of the second point
    :param miles: Distance should be in miles or kilometers?
    :return: Returns distance in meters between the two points on the Earth
    :rtype: float
    """
    if len(point1) != 2 or len(point2) != 2:
        raise ValueError("Function expects two points with a latitude and longtitude")
    lat1 = radians(float(point1[0]))
    lon1 = radians(float(point1[1]))
    lat2 = radians(float(point2[0]))
    lon2 = radians(float(point2[1]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    if miles:
        d = EARTH_RADIUS_MILES * c
    else:
        d = EARTH_RADIUS_METERS * c
    return d

if __name__ == "__main__":
    import doctest
    doctest.testmod()

