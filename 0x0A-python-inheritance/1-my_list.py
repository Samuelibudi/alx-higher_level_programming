#!/usr/bin/python3
"""Module defines class Mylist that inherits from class list"""


class MyList(list):
    """Class that inherits from class list"""

    def print_sorted(self):
        """Method that prints sorted list"""
        print(self.sort())
