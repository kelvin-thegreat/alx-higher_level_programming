#!/usr/bin/python3
"""

Module composed of a function that adds two numbers


"""


def add_integer(a, b=98):
    """ function that Returns the sum of two integers.

    Arguments:
    a -- an integer or a float.
    b -- an integer or a float. Default is 98.

    Returns:
    an integer, the sum of a and b.

    Raises:
    TypeError: if a or b is non-integer or not of float type

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
