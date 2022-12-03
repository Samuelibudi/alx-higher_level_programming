#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for c in range(len(matrix[0])):
            if c != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][c]), end='')
        print()
