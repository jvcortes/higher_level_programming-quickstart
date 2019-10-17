#!/usr/bin/python3
"""
This module contains the function definition for task 6.
"""
import json


def from_json_string(my_str):
    """ returns an object from a JSON string

    Args:
        my_str (str): JSON string
    """
    return json.loads(my_str)
