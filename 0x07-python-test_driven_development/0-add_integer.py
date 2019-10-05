#!/usr/bin/python3
"""

This module contains the function definition for task 0.

"""


def add_integer(a, b=98):
    """ Returns the integer sum of two provided numbers.

    Args:
        a (int, float): First number.
        b (int, float): Second number (default: 98)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(round(a + b))
