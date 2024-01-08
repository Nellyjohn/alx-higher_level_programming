#!/usr/bin/python3
"""This is a module of class base geometry"""


class BaseGeometry:
    """Class base eometry"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value.

        Args:
            self: first parameter.
            name (string): second parameter.
            value (int): third parameter.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.

        Returns:
            nothing.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
