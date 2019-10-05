#!/usr/bin/python3
"""

This module contains the function definition for task 5.

"""


def text_indentation(text):
    """Prints a text with two new line characters after:
        - A period character (``.``).
        - A colon character (``:``).
        - A question mark character (``?``)

    Args:
        text (str): text to print
    """
    result = ""
    if isinstance(text, str):
        if text:
            for c in text:
                result += c
                if c in ('?', '.', ':'):
                    result = result.strip(" ")
                    print(result, end='\n\n')
                    result = ""
            result = result.strip(" ")
            print(result, end='')
    else:
        raise TypeError("text must be a string")
