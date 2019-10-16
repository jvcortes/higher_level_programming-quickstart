#!/usr/bin/python3
"""
This module contains the function definition for task 13
"""


def add_attribute(obj, name, value):
    """ Attempts to add a new attribute to an object.

    Args:
        obj (object): provided object
        name (str): name for the attribute
        value (object): value for the attribute

    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
