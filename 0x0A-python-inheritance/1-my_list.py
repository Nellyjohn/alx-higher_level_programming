#!/usr/bin/python3
"""This module defines a subclass that inherits from a class"""


class MyList(list):
    """Class Mylist"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
