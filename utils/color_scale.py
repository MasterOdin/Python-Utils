def probability_to_red_green(probability, flip=False):
    """
    Given a probability [0, 1], it returns the associated RGB value that corresponds to a
    red -> green color scale. This

    >>> probability_to_red_green(0)
    (255, 0, 0)
    >>> probability_to_red_green(1)
    (0, 255, 0)
    >>> probability_to_red_green(0.6)
    (102, 153, 0)
    >>> probability_to_red_green(0, True)
    (0, 255, 0)
    >>> probability_to_red_green(1, True)
    (255, 0, 0)

    :param probability:
    :param flip:
    :return:
    """
    n = probability * 100
    red = int((255. * (100 - n)) / 100.)
    green = int((255. * n) / 100)
    blue = 0
    if flip:
        return green, red, blue
    else:
        return red, green, blue

if __name__ == "__main__":
    import doctest
    doctest.testmod()
