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
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Represents objects as a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
