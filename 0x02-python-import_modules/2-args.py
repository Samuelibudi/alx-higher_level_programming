#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n_args = len(sys.argv) - 1
    if (n_args == 0):
        print("{} arguments.".format(n_args))
    elif (n_args == 1):
        print("{} argument:".format(n_args))
    else:
        print("{} arguments:".format(n_args))

    if n_args >= 1:
        n_args = 0
        for i in sys.argv:
            if n_args != 0:
                print("{}: {}".format(n_args, i))
            n_args += 1
