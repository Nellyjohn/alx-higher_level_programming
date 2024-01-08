#!/usr/bin/python3
"""This is a boolean module"""


def inherits_from(obj, a_class):
    """Returns true if an object is an instance of a
    class that inherited directly or indirectly from a specified class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
