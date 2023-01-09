#!/usr/bin/python3
"""Method checks if object is an instance of,
    or if the object is ana instance of a class,
    that inherited from the specified class."""


def is_kind_of_class(obj, a_class):
    """Function that checks if obj is instance of a_class."""
    return isinstance(obj, a_class)
