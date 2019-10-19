#!/usr/bin/python3
"""
This module contains the function definition for task 15.
"""


def append_after(filename="", search_string="", new_string=""):
    """ appends a new string after a the lines that contain a
    specified string inside a file.

    Args:
        filename (str): name of the JSON file
        search_string (str): string to search
        new_string (str): string to append
    """
    with open(filename, "r+") as f:
        content = f.readlines()
        new_content = ""
        for line in content:
            new_line = line
            if search_string in line:
                new_line += new_string
            new_content += new_line
        f.truncate(0)
        f.seek(0)
        f.write(new_content)
