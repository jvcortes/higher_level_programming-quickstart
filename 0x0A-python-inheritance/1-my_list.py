#!/usr/bin/python3
"""

This module holds the class definition for task 1

"""


class MyList(list):
    """Example class that extends from ``list``. """

    def print_sorted(self):
        """ Prints the contents of the list, in ascending order. """
        print(sorted(self))
