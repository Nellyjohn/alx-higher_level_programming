#!/usr/bin/python3
""" This is an attributes and methods module """


def lookup(obj):
    """ Returns a list of attributes and methods of an object """
    return (list([attr for attr in dir(obj)]))
