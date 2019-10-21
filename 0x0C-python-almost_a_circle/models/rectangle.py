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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: width of the Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: height of the Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: x position of the Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """int: y position of the Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
