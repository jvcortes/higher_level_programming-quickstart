#!/usr/bin/python3
"""
This module contains the function definition for task 5.
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object

    Args:
        my_obj (object): provided object
    """
    return json.dumps(my_obj)
