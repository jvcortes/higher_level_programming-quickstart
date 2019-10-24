#!/usr/bin/python3
"""
Module for the Base class.
"""
import json


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
        if list_dictionaries and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes its JSON representation to a file.

        Args:
            list_objs: list of objects
        """

        with open("{}.json".format(cls.__name__), "w+") as fi:
            if list_objs and list_objs is not None:
                fi.write(str(list(cls.to_json_string(x.to_dictionary())
                                  for x in list_objs)))
            else:
                fi.write(cls.to_json_string("[]"))
