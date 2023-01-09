#!/usr/bin/python3
"""An empty class BaseGeometry."""


class BaseGeometry:
    """A class BaseGeomtry"""

    def area(self):
        """Function that defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that receives the value property."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
