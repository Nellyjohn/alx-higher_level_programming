#!/usr/bin/python3
"""This module represents a class rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Represents class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method.
        Args:
            width (int): first parameter.
            height (int): second parameter.
            x (int): third parameter. Default value is 0.
            y (int): fourth parameter. Default value is 0.
            id (int): fifth parameter.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Doc function"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Doc function"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Doc function"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
             raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Doc function"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        result = self.height * self.width
        return (result)
