#!/usr/bin/python3
"""Module defines class Square based on Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square from rectangle class"""

    def __init__(self, size):
        """Method that initializes a Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.size, self.size)

    def area():
        """Method that returns a string with the area"""
        return super().area()
