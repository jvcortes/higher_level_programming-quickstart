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

    def update(self, *args, **kwargs):
        """ Updates a Square instance with non-keyworded/keyword args.

        Args:
            1, id (int): new id for the square
            2, size (int): new size for the square
            3, x (int): new x position for the square
            4, y (int): new y position for the square

        The arguments should comply with their respective requirements.
        """

        if args:
            attrs = ("id", "size", "x", "y")
            for idx, arg in enumerate(args):
                if idx >= len(attrs):
                    break
                if hasattr(self, attrs[idx]):
                    setattr(self, attrs[idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the square. """
        rep = {'id': 0, 'size': 0, 'x': 0, 'y': 0}
        for key, _ in rep.items():
            if hasattr(self, key):
                rep[key] = getattr(self, key)

        return rep

    @property
    def size(self):
        """ int: returns the width of the square.

        The setter function will set the width and the height of the square
        with the same value.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns the square string representation. """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)
