#!/usr/bin/python3
"""
This module contains the function definition for task 1.
"""


def number_of_lines(filename=""):
    """ prints the contents of a file.

    Args:
        filename (str): file name
    """
    with open(filename, 'r') as f:
        return len(f.readlines())
