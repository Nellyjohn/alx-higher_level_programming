#!/usr/bin/python3
"""This module defines a class that inherits from another class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class base geometry"""
    def __init__(self, width, height):
        """Defines a subclass.
        Args:
            self: first parameter.
            width (int): second parameter.
            height (int): third parameter.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
