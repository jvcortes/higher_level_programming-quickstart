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

    def __lt__(self, other):
        """Compares the instance size with another Square instance size.

        Checks wheter the instance size is strictly smaller than the other
        instance size or not.
        """
        if not isinstance(other, Square):
            return NotImplemented

        return self.size < other.size

    def __le__(self, other):
        """Compares the instance size with another Square instance size.

        Checks wheter the instance size is less or equal than the other
        instance size or not.
        """
        if not isinstance(other, Square):
            return NotImplemented

        return self.size <= other.size

    def __eq__(self, other):
        """Compares the instance size with another Square instance size.

        Checks if the instance size is equal than the other instance size.
        """
        if not isinstance(other, Square):
            return NotImplemented

        return self.size == other.size

    def __ne__(self, other):
        """Compares the instance size with another Square instance size.

        Checks wheter the instance size is not equal than the
        other instance size or not.
        """
        if not isinstance(other, Square):
            return NotImplemented

        return self.size != other.size

    def __gt__(self, other):
        """Compares the instance size with another Square instance size.

        Checks wheter the instance size is strictly greater than the
        other instance size or not.
        """
        if not isinstance(other, Square):
            return NotImplemented

        return self.size > other.size

    def __ge__(self, other):
        """Compares the instance size with another Square instance size.

        Checks wheter the instance size is greater or equal than the
        other instance size or not.
        """
        if not isinstance(other, Square):
            return NotImplemented

        return self.size >= other.size

    @property
    def size(self):
        """int: size of the Square instance

        Size should be an integer of value zero or greater.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the area of the square """
        return self.size ** 2
