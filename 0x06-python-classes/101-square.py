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
    def __init__(self, size=0, position=(0, 0)):
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

        if isinstance(position, tuple) and len(position) == 2:
            for i in position:
                if not isinstance(i, int) or i < 0:
                    raise TypeError("position must be a tuple of 2 positive"
                                    " integers")
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """tuple: position for the square

        The position has to be a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            for i in value:
                if not isinstance(i, int) or i < 0:
                    raise TypeError("position must be a tuple of 2 positive"
                                    "integers")
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns the area of the square."""
        return self.size ** 2

    def __str__(self):
        """ Returns the square string representation.

        If the Square instance contains a position it will be printed as
        follows:
            - The first element of the position will be represented as spaces
              before the square.
            - The second element of the position will be represented as newline
              characters before the square.

        The square itself will be composed of '#' characters.
        """
        s = ""
        if self.size:
            if self.position[1]:
                for _ in range(self.position[1]):
                    s += '\n'
            for i in range(self.size):
                if self.position[0]:
                    for _ in range(self.position[0]):
                        s += ' '
                for _ in range(self.size):
                    s += '#'
                if i < self.size - 1:
                    s += '\n'

        return s

    def my_print(self):
        """ Prints the square string representation to the standard output."""

        print(self.__str__)
