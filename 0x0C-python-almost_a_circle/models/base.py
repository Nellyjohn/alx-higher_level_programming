#!/usr/bin/python3
"""This is a Base module"""
import json
from os.path import isfile
import csv
import turtle
import os


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

    @staticmethod
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
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        This is a static method that retyurns the list of the
        JSON string representation
        """
        if json_string is None or not json_string:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        This is a class method that returns an
        instance with all attribures already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """
        This is a class method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_instances = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                contents = file.read()
                list_dictionaries = cls.from_json_string(contents)
                list_instances = []
                for dictionary in list_dictionaries:
                    list_instances.append(cls.create(**dictionary))
        return (list_instances)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This is a class method that serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        try:
            my_turtle = turtle.Turtle()
            my_turtle.screen.bgcolor("#b7312c")
            my_turtle.pensize(3)
            my_turtle.shape("turtle")

            my_turtle.color("ffffff")
            for rect in list_rectangles:
                my_turtle.showturtle()
                my_turtle.up()
                my_turtle.goto(rect.x, rect.y)
                my_turtle.down()
                for i in range(2):
                    my_turtle.forward(rect.width)
                    my_turtle.left(90)
                    my_turtle.forward(rect.height)
                    my_turtle.left(90)
                my_turtle.hideturtle()

            my_turtle.color("#b5e3d8")
            for sq in list_squares:
                my_turtle.showturtle()
                my_turtle.up()
                my_turtle.goto(sq.x, sq.y)
                my_turtle.down()
                for i in range(4):
                    my_turtle.forward(sq.width)
                    my_turtle.left(90)
                    my_turtle.forward(sq.height)
                    my_turtle.left(90)
                my_turtle.hideturtle()

            turtle.exitonclick()
        except Exception:
            print("Goodbye")
