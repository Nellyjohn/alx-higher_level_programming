#!/usr/bin/python3
# Auth: Vivian Okaforcha
"""Defines a square"""


class Square:
    """Initialize a square
    Args:
        size: size of the square
    Raises:
        TypeError if size is not an integer
        ValueError if size less than 0
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """Calculates the area of a square
    Returns:
        The current square area
    """
    def area(self):
	    return (self.__size ** 2)
