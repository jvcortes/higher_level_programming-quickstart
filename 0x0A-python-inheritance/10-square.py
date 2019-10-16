#!/usr/bin/python3
"""

This module holds the class definition for task 10

"""
"""
perhaps i should import the function before declaring the class.
"""


class Square(__import__("9-rectangle").Rectangle):
    """ Defines a size.

        Args:
            size (int): size of the square

        Attributes:
            size (int): size of the square
    """

    def __init__(self, size):
        """ Instanciates a Rectangle object.

        Args:
            square (int): size of the square, must be greater than zero.
        """

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """ Returns the area of the shape. """
        return self.__size ** 2

    def __str__(self):
        """ Returns the string representation of the square. """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
