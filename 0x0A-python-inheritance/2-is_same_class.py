#!/usr/bin/python3
""" This module checks for an object's instance """


def is_same_class(obj, a_class):
    """Returns True if an object is an instance of a class,"
    else return false"""
    return (type(obj) == a_class)
