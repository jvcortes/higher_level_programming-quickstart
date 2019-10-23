#!/usr/bin/python3
"""
Module for the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square

    Args:
        size (int): size of the Square
        x (int): horizontal position of the Square
        y (int): vertical position of the Square
        id (int): id of the Square instance

    Attributes
        width (int): width of the Square
        height (int): height of the Square
        x (int): horizontal position of the Square
        y (int): vertical position of the Square
        __nb_objects (int): count of currently active, id-less Base instances
        id (int): id of the Square instance
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance.

        Args:
            size (int): size for the Square instance
            x (int): horizontal position for the Square instance
            y (int): vertical position for the Square instance
            id (int): id of the Square instance

        """

        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the square string representation. """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)
