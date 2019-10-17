#!/usr/bin/python3
"""
This module contains the function definition for task 7.
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object JSON representation to a file

    Args:
        my_obj (object): provided object
        filename (str): name for the file
    """
    with open(filename, "w+") as json_f:
        json_f.write(json.dumps(my_obj))
