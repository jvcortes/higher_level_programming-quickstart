#!/usr/bin/python3
"""

This module holds the function definition for task 4

"""


def inherits_from(obj, a_class):
    """Checks if an object extends from a specified class.

    Args:
        obj (object): provided object
        a_class (object): provided class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
