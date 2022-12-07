#!/usr/bin/python3

def best_score(a_dictionary):
    keys = list(a_dictionary.keys())

    big_int = 0

    for i in keys:
        if big_int < a_dictionary[i]:
            big_int = a_dictionary[i]

    if big_int != 0:
        return big_int
    else:
        return None
