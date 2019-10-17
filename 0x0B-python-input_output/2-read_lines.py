#!/usr/bin/python3
"""
This module contains the function definition for task 2.
"""


def read_lines(filename="", nb_lines=0):
    """ reads and prints the first n lines of a file

    Args:
        filename (str): file name
        nb_lines (int): number of lines
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end='')
        else:
            for n, line in enumerate(f):
                if n >= nb_lines:
                    break
                print(line, end='')
