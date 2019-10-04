#!/usr/bin/python3
"""

This module contains the function definition for task 0.

"""


def add_integer(a, b=98):
    """ Returns the sum of two provided numbers.

    Args:
        a (int, float): First number.
        b (int, float): Second number (default: 98)
    """
    if isinstance(a, (int, float)):
        result = a
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        result += b
    else:
        raise TypeError("b must be an integer")
    return result
