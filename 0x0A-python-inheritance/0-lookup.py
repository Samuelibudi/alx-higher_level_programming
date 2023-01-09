#!/usr/bin/python3
"""Module defines a function that looks up object attributes"""


def lookup(obj):
    """Function returns the list of available attributes

    and methods of an object"""

    return dir(obj)
