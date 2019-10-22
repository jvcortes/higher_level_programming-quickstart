#!/usr/bin/python3
"""
Module for the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle

    Args:
        width (int): width of the Rectangle
        height (int): height of the Rectangle
        x (int): horizontal position of the Rectangle
        y (int): vertical position of the Rectangle
        id (int): id of the Rectangle instance

    Attributes
        width (int): width of the Rectangle
        height (int): height of the Rectangle
        x (int): horizontal position of the Rectangle
        y (int): vertical position of the Rectangle
        __nb_objects (int): count of currently active, id-less Base instances
        id (int): id of the Rectangle instance

    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """int: returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints its representation to the standard output."""
        for i in range(0, self.__height):
            for _ in range(0, self.__width):
                print('#', end='')
            if i < self.__height - 1:
                print()

    @property
    def width(self):
        """int: width of the Rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """int: height of the Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """int: x position of the Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, value):

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """int: y position of the Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, value):

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
