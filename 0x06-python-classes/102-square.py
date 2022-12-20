#!/usr/bin/python3

"""Defintion of a class"""


class Square:
    """Class that defines a square by its size"""

    def __init__(self, size=0):
        """Method to initialise square object"""

        self.size = int(size)

    @property
    def size(self):
        """ Method to return the size value"""

        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value of the square object"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparison to a square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison toa square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a square."""
        return self.area() >= other.area()
