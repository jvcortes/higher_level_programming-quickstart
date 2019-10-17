#!/usr/bin/python3
"""
This module contains the function definition for task 3.
"""


def append_write(filename="", text=""):
    """ appends a string to a file

    Args:
        filename (str): file name
        nb_lines (int): number of lines
    """
    with open(filename, 'a+') as f:
        return f.write(text)
