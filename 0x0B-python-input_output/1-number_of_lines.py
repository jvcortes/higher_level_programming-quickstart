#!/usr/bin/python3
"""
This module contains the function definition for task 1.
"""


def number_of_lines(filename=""):
    """ returs the number of lines of a file

    Args:
        filename (str): file name
    """
    with open(filename, 'r') as f:
        return len(f.readlines())
