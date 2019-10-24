#!/usr/bin/python3
"""
Module for the Base class.
"""
import json
import os


class Base:
    """
    Defines a Base class.

    Args:
        id (int): id of the Base instance

    Attributes
        __nb_objects (int): count of currently active, id-less Base instances
        id (int): id of the Base instance

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a Base instance.

        Args:
            id (int): id of the Base instance
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON representation of a list of dictionaries.

        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list from a JSON representation.

        Args:
            json_string (str): JSON representation of the object.
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes its JSON representation to a file.

        Args:
            list_objs: list of objects
        """

        with open("{}.json".format(cls.__name__), "w+") as fi:
            if list_objs:
                fi.write(cls.to_json_string(
                    [x.to_dictionary() for x in list_objs]))
            else:
                fi.write("[]")

    @classmethod
    def load_from_file(cls):
        """ Loads an instance from JSON representation in a file."""

        instances = []
        if os.path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), "r") as fi:
                li = json.loads(fi.read())
                for dic in li:
                    instances.append(cls.create(**dic))
        return instances

    @classmethod
    def create(cls, **dictionary):
        """ Instantiates a Base object from a dictionary.

        Args:
            dictionary (dict): dictionary of attributes for the instance.
        """

        if dictionary:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
                instance.update(**dictionary)
            else:
                instance = cls(1)
                instance.update(**dictionary)
            return instance
