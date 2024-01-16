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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Doc function"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Doc function"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Doc function"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of rectangle"""
        result = self.height * self.width
        return (result)

    def display(self):
        """prints # to stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Represents objects as a string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Function Doc
        """

        return {'id': self.id, 'x': self.x, 'width': self.width,
                'height': self.height, 'y': self.y}
