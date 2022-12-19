#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as i:
        print("Exception: {}".format(i), file=stderr)
        result = None
    finally:
        return (result)
