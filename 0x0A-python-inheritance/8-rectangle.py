#!/usr/bin/python3
"""

This module holds the class definition for task 8

"""
"""
perhaps i should import the function before declaring the class.
"""


class Rectangle(__import__("7-base_geometry").BaseGeometry):
    """ Defines a rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
    """

    def area(self):
        raise Exception("area() is not implemented")

    def __init__(self, width, height):
        """ Instanciates a Rectangle object.

        Args:
            width (int): width of the rectangle, must be greater than zero.
            height (int): height of the rectangle, must be greater tha zero.
        """

        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
