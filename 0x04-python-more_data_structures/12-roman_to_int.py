#!/usr/bin/python

def roman_to_int(roman_string):
    lst = []
    dec_num = 0

    for let in roman_string:
        lst.append(let)

    for i in range(len(lst)):
        if lst[i] == 'I' and lst[i + 1] != 'V' and lst[i + 1] != 'X':
            dec_num += 1
        else:
            dec_num -= 1

        if lst[i] == 'V':
            dec_num += 5

        if lst[i] == 'X' and lst[i + 1] != 'L' and lst[i + 1] != 'C':
            dec_num += 10
        else:
            dec_num -= 10

        if lst[i] == 'L':
            dec_num += 50

        if lst[i] == 'C' and lst[i+1] != 'D' and lst[i+1] != 'M':
            dec_num += 100
        else:
            dec_num -= 100

        if lst[i] == 'D':
            dec_num += 500

        if lst[i] == 'M':
            dec_num += 1000
    return dec_num
