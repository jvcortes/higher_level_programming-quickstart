#!/usr/bin/python3
"""

This module holds the function definition for task 0

"""


class BaseGeometry():
    """ Defines an empty Geometry object. """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value.

        Args:
            name (str): name for the value
            value (int): provided value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an greater than 0".format(name))
