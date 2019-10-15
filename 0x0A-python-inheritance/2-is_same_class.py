#!/usr/bin/python3
"""

This module holds the function definition for task 2

"""


def is_same_class(obj, a_class):
    """ Checks if an object is exactly an instance of an specified class.

    Args:
        obj (object): provided object
        a_class (object): provided class
    """
    return type(obj) is a_class
