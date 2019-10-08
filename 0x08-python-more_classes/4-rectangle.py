#!/usr/bin/python3
"""
This module defines the rectangle class.
"""


class Rectangle:
    """
    Defines an empty Rectangle class.

    Args:
        width (int): width for the Rectangle instance.
        height (int): height for the Rectangle instance.

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with its attributes.

        Args:
            width (int): width for the Rectangle instance.
            height (int): height for the Rectangle instance.

        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    def __str__(self):
        """ Returns the string representation of the rectangle. """

        s = ""

        if 0 not in (self.width, self.height):
            for i in range(self.height):
                for _ in range(self.width):
                    s += '#'
                if i < self.height - 1:
                    s += '\n'

        return s

    def __repr__(self):
        """ Returns the printable representation of the rectangle instance. """

        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """int: Width of the Rectangle instance.

        Width has to be an integer with a value equal or greater than zero.
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: Height of the Rectangle instance.

        Height has to be an integer with a value equal or greater than zero.
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns the area of the square. """

        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of the square. """

        return (self.height * 2) + (self.width * 2) if any(
            (self.height > 0, self.width > 0)) else 0
