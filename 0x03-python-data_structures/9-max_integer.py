#!/usr/bin/python3

def max_integer(my_list=[]):
    big_int = my_list[0]
    if len(my_list) == 0:
        return None
    
    for i in range(1, len(my_list)):
       if my_list[i] > big_int:
             big_int = my_list[i]
    return big_int