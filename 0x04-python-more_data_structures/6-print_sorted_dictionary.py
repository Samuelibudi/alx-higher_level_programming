#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(sorted(a_dictionary.items()))

    for k, v in a_dictionary.items():
        print("{}: {}".format(k, v))
