#!/usr/bin/python3

def uniq_add(my_list=[]):
    lst = set(my_list)
    result = 0
    for i in lst:
        result += i
    return result
