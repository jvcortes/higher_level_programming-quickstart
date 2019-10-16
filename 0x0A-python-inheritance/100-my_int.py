#!/usr/bin/python3
"""

This module holds the class definition for task 12

"""


class MyInt(int):
    """ Defines an integer object.

    """

    def __eq__(self, other):

        return int(self) != int(other)

    def __ne__(self, other):

        return int(self) == int(other)
