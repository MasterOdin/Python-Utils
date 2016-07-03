# -*- coding: utf-8 -*-

# The Metric and Imperial units that are currently supported within the conversion methods
UNITS = {
    "ym": "yoctometre",
    "zm": "zeptometre",
    "am": "attometre",
    "fm": "femtometre",
    "pm": "picometre",
    "nm": "nanometre",
    "µm": "micrometre",
    "mm": "millimetre",
    "cm": "centimetre",
    "dm": "decimetre",
    "m":  "metre",
    "dam": "decametre",
    "hm": "hectometre",
    "km": "kilometre",
    "Mm": "megametre",
    "Gm": "gigametre",
    "Tm": "terametre",
    "Pm": "petametre",
    "Em": "exametre",
    "Zm": "zettametre",
    "Ym": "yottametre",
    "in": "inch",
    "ft": "foot",
    "yd": "yard",
    "mi": "mile",
    "fur": "furlong",
    "lea": "league",
    "ftm": "fathom"
}

# What you need to mulitply each unit against to convert it to meters
UNITS_TO_METERS = {
    "ym": 1*(10**-24),
    "zm": 1*(10**-21),
    "am": 1*(10**-18),
    "fm": 1*(10**-15),
    "pm": 1*(10**-12),
    "nm": 1*(10**-9),
    "µm": 1*(10**-6),
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m":  1,
    "dam": 10,
    "hm": 100,
    "km": 1000,
    "Mm": 1000000,
    "Gm": 1*(10**9),
    "Tm": 1*(10**12),
    "Pm": 1*(10**15),
    "Em": 1*(10**18),
    "Zm": 1*(10**21),
    "Ym": 1*(10**24),
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34,
    "fur": 201.168,
    "lea": 5556,
    "ftm": 1.8288
}

# What you need to multiply each unit by to get to the unit from meters
UNITS_FROM_METERS = {
    "ym": 1*(10**24),
    "zm": 1*(10**21),
    "am": 1*(10**18),
    "fm": 1*(10**15),
    "pm": 1*(10**12),
    "nm": 1*(10**9),
    "µm": 1*(10**6),
    "mm": 1000,
    "cm": 100,
    "dm": 10,
    "m":  1,
    "dam": 0.1,
    "hm": 0.01,
    "km": 0.001,
    "Mm": 1*(10**-6),
    "Gm": 1*(10**-9),
    "Tm": 1*(10**-12),
    "Pm": 1*(10**-15),
    "Em": 1*(10**-18),
    "Zm": 1*(10**-21),
    "Ym": 1*(10**-24),
    "in": 39.3701,
    "ft": 3.28084,
    "yd": 1.09361,
    "mi": 0.000621371,
    "fur": 0.00497096,
    "lea": 0.000179986,
    "ftm": 0.546807
}


def convert(length, from_unit="cm", to_unit="in"):
    """
    Given a length this will convert the length to a float and then convert it from the from_unit
    to the to_unit specified. If either unit is non-existant in the UNITS dictionary, a KeyError
    will be raised.

    >>> convert(5, from_unit="m", to_unit="fur")
    0.0248548
    >>> convert(0, from_unit="fake")
    Traceback (most recent call last):
        ...
    KeyError: 'fake'

    >>> convert(0, to_unit="fake")
    Traceback (most recent call last):
        ...
    KeyError: 'fake'

    :param length:
    :param from_unit:
    :param to_unit:
    :return:
    :rtype: float
    """
    length = float(length)
    if from_unit == to_unit:
        return length

    return length * UNITS_TO_METERS[from_unit] * UNITS_FROM_METERS[to_unit]


def get_micro_symbol():
    """
    Utility function to just return the micro character so I don't have to copy/paste it from
    this file everytime I need it

    :return: 'µ'
    """
    return "µ"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
