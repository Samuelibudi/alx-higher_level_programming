#!/usr/bin/python3
"""Module defines function that checks if an object 
    is an instance of a class that inherited(directly
    or indirectly) from the specicified class."""


def inherits_from(obj, a_class):
    """functions checks if obj is an instance of a_class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
