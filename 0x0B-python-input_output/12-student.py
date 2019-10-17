#!/usr/bin/python3
"""
This module contains the class definition for task 12.
"""


class Student:
    """ Defines a student

    Args:
        first_name (str): student's first name
        last_name (str): student's last name
        age (int): student's age

    Attributes:
        first_name (str): student's first name
        last_name (str): student's last name
        age (int): student's age
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a Student instance

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the Student instance's dictionary.

        Args:
            attrs (list: str): list of attributes to retrieve, if the list is
            empty, the function will retrieve all the attributes.
        """

        if attrs is None or attrs == 0:
            return self.__dict__
        return dict(filter(lambda x: x[0] in attrs, self.__dict__.items()))
