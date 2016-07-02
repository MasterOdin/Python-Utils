# -*- coding: utf-8 -*-

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
    "mi": "mile"
}

UNITS_TO_METERS = {
    "cm": 0,
    "dm": 0,
    "m":  1
}

UNITS_FROM_METERS = {
    "m": 1

}



def convert(length, from_unit="cm", to_unit="in"):
    """
    Given a length this will convert the length to a float and then convert it from the from_unit
    to the to_unit specified. If either unit is non-existant in the UNITS dictionary, a KeyError
    will be raised.

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
