#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for temp in my_list:
        num += temp[0] * temp[1]
        den += temp[1]

    return (num / den)
