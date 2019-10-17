#!/usr/bin/python3
"""
This module contains the function definition for task 7.
"""
import json


def load_from_json_file(filename):
    """ creates an object from a JSON file

    Args:
        filename (str): name of the JSON file
    """
    with open(filename, "r") as json_f:
        return json.loads(json_f.read())
