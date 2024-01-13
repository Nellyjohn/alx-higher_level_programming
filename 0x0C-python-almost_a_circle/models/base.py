#!/usr/bin/python3
"""This is a Base module"""


class Base:
    """Represents Base with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing.
        Args:
            id (int): first parameter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
