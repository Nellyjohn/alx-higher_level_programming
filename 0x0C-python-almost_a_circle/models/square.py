#!/usr/bin/python3
"""class square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method.
        Args:
            size (int): first parameter
            x (int): second parameter.
            y (int): third parameter.
            id (int): fourth parameter.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update"""
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            valid_attributes = ['id', 'size', 'x', 'y']
            for key, value in kwargs.items():
                if key in valid_attributes:
                    if key == 'size':
                        for i in ["width", "height"]:
                            exec("self.{} = {}".format(i, value))
                            continue
                    exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Represents objects as a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
