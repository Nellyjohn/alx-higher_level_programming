#!/usr/bin/python3

""" This is an addition module """

def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a (int): first parameter.
        b (int): second parameter. Defaults to 98.

    Raises:
        TypeError: if either a or b is a not_integer or float.
    Returns:
        int: The sum of the two integers.
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
