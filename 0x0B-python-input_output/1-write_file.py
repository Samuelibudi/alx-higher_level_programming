#!/usr/bin/python3
""" Module that contains a function that returns the number of lines
    of a text file
"""


def number_of_lines(filename="", text=""):
    """ Function that reads from a file and prints its number of lines """
    
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
