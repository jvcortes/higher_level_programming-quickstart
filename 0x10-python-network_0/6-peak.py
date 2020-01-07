#!/usr/bin/python3
"""
Module for task 6.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in an unsorted list of integers.

    Arguments:
        list_of_integers (list): list of integers.
    """

    if not list_of_integers or not isinstance(list_of_integers, list):
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    c = 0
    while c < len(list_of_integers):
        if c == len(list_of_integers) - 1:
            return list_of_integers[c]

        if list_of_integers[c] >= list_of_integers[c+1]:
            if c == 0 or list_of_integers[c-1] <= list_of_integers[c]:
                return list_of_integers[c]
            c += 2

        if list_of_integers[c] <= list_of_integers[c+1]:
            c += 1
