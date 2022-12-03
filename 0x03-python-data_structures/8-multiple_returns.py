#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        first_ch = None
    else:
        first_ch = sentence[0]
    length = len(sentence)

    new_tuple = (length, first_ch)

    return new_tuple
