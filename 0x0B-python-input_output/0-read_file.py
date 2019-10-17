#!/usr/bin/python3
"""
This module contains the function definition for task 0.
"""


def read_file(filename=""):
    """ prints the contents of a file.

    Args:
        filename (str): file name
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
