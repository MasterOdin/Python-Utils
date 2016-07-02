def celsius_to_fahrenheit(degrees):
    """
    Given a temperature in celsius, return it in fahrenheit

    :param degrees:
    :return:
    """
    return (degrees * 1.8) + 32.


def fahrenheit_to_celsius(degrees):
    """
    Given a temperature in fahrenheit, return it in celsius

    :param degrees:
    :return:
    """
    return (degrees - 32.) / 1.8

if __name__ == "__main__":
    import doctest
    doctest.testmod()
