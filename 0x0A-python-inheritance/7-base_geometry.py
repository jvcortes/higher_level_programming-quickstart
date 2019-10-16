#!/usr/bin/python3
"""

This module holds the class definition for task 7

"""


class BaseGeometry():
    """ Defines an Geometry object. """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value.

        Args:
            name (str): name for the value
            value (int): provided value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
