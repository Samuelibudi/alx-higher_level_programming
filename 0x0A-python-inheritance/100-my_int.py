#!/usr/bin/python3
"""Module defines class that inherits from int"""


class MyInt(int):
    """Class inherits form class int"""

    def __eq__(self, other):
        """Method that returns != check"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Method that returns == check"""
        return int.__eq__(self, other)
