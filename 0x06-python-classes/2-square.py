#!/usr/bin/python3

"""Definition of a square"""


class Square:
    """Class that defines a square by its size"""

    def __init__(self, size=0):
        """Method to initialise square object
        Args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            rasie TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
