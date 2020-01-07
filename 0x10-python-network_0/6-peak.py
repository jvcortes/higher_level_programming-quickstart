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

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return (list_of_integers[0]
                if list_of_integers[0] >= list_of_integers[1]
                else list_of_integers[1])
    if not list_of_integers:
        return None

    c = 1
    while c < len(list_of_integers):
        if (list_of_integers[c-1] <= list_of_integers[c]
                >= list_of_integers[c+1]):
            return list_of_integers[c]

        if list_of_integers[c] <= list_of_integers[c+1]:
            c += 1
        else:
            c += 2
