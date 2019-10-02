#!/usr/bin/python3
"""

This module contains the Square class

"""


class Square:
    """ Defines a square

    Args:
        size (int): Initial size of the square

    Attributes:
        size (int): Size of the square

    """
    def __init__(self, size=0):
        """ Initializes a Square type object

        Args:
            size (int, optional): Initial size of the square with a
                default value of zero. If the size is less than zero,
                the function will raise a ValueError exception.

        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
