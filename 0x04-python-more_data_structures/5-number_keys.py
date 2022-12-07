#!/usr/bin/python3

def number_keys(a_dictionary):
    num_keys = 0
    for k, v in a_dictionary.items():
        num_keys += 1

    return num_keys
