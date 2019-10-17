#!/usr/bin/python3
"""
This module contains the function definition for task 10.
"""


def class_to_json(my_obj):
    """ returns a class dictionary description JSON representation to a file

    Args:
        my_obj (object): provided object
        filename (str): name for the file
    """
    return my_obj.__dict__
