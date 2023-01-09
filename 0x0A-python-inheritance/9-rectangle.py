#!/usr/bin/python3
"""Module that defines a class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class defines a rectangle from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method returns instance area"""
        return self.__width * self.__height

    def __str__(self):
        """special method that returns the prinatble string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
