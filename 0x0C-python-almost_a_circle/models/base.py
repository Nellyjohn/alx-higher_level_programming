#!/usr/bin/python3
"""This is a Base module"""
import json


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

    def to_json_string(list_dictionaries):
        """
        This is a static method that returns the JSON string representation 
        of list_dictionaries which is a list of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            to_json_string = json.dumps(list_dictionaries)
            return (to_json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This is a class method that writes the JSON string 
        representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
            to_json_string = json.dumps(list_objs)
            return (to_json_string)
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
                f.write(Base.to_json_string(list_objs))
