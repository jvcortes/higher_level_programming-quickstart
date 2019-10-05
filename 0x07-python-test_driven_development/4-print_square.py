#!/usr/bin/python3
"""

This module contains the function definition for task 3.

"""


def print_square(size):
    """ Prints a square of a determined size with the character '#'.

    Args:
        size (int): size of the square.
    """

    if isinstance(size, int):
        if size >= 0:
            for _ in range(size):
                for _ in range(size):
                    print("#", end='')
                print()
        else:
            raise ValueError("size must be >= 0")
        print()
    else:
        raise TypeError("size must be an integer")
