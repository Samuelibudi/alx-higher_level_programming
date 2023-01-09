#!/usr/bin/python3
"""Module defines method to check if
    object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """checks if object is exact instance of class"""
    return type(obj) is a_class
