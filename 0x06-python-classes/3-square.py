#!/usr/bin/python3
# Auth: Vivian Okaforcha
"""Defines a square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size: size of the square
        Raises:
            TypeError if size is not an integer
            ValueError if size less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates the area of a square

        Returns:
            int: The current square area
        """

        return (self.__size ** 2)
