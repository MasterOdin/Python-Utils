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


def rgb_to_int(red, green, blue):
    """
    Given RGB components of a color, covnert this to an integer
    which is in the range of 0 (#000000) to 16777215 (#FFFFFF)

    >>> rgb_to_int(0, 0, 0)
    0
    >>> rgb_to_int(255, 0, 0)
    16711680
    >>> rgb_to_int(0, 255, 0)
    65280
    >>> rgb_to_int(0, 0, 255)
    255
    >>> rgb_to_int(255, 255, 255)
    16777215
    """
    return (red << 16) + (green << 8) + blue


def int_to_rgb(rgb_int):
    """
    Given an integer, converts to to RGB value. Any integer outside
    the range of (0, 16777215) will raise an invalid
    >>> int_to_rgb(-1)
    Traceback (most recent call last):
    ...
    ValueError: Integer must be in range [0, 16777215], got -1.
    >>> int_to_rgb(0)
    (0, 0, 0)
    >>> int_to_rgb(255)
    (0, 0, 255)
    >>> int_to_rgb(65280)
    (0, 255, 0)
    >>> int_to_rgb(16711680)
    (255, 0, 0)
    >>> int_to_rgb(16777215)
    (255, 255, 255)
    >>> int_to_rgb(20000000)
    Traceback (most recent call last):
    ...
    ValueError: Integer must be in range [0, 16777215], got 20000000.
    """
    if rgb_int < 0 or 16777215 < rgb_int:
        raise ValueError('Integer must be in range [0, 16777215], got {}.'.format(rgb_int))
    blue =  rgb_int & 255
    green = (rgb_int >> 8) & 255
    red =   (rgb_int >> 16) & 255
    return red, green, blue
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
