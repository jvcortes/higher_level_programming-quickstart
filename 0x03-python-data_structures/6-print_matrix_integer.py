#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if matrix:
        for i in matrix:
            for j, item in enumerate(i):
                print("{:d}".format(item), end="")
                if j < len(i) - 1:
                    print(" ", end="")
            print("")
