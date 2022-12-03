#!/usr/bin/python3

def max_integer(my_list=[]):
    big_int = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] > big_int:
                big_int = my_list[i]
    return big_int
