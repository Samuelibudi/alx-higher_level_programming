#!/usr/bin/pyhton3
"""Module has a function that adds two numbers"""

def add_integer(a, b=98):
    """ Function that adds two integers or floats

    Args:
        a: first number
        b: second number

    Returns:
        The sum of the two numbers.

    Raises:
        TypeError: If a or b are not integers or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
