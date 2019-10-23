#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"""
This module contains the unit tests for the `Rectangle` class.
"""


class RectangleToDictTest(unittest.TestCase):
    """
    Defines the test cases for the `Rectangle` class
    """

    def setUp(self):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_to_simple_dict(self):
        instance = Rectangle(4, 8)
        self.assertEqual(instance.to_dictionary(),
                         {
                             'id': 1,
                             'width': 4,
                             'height': 8,
                             'x': 0,
                             'y': 0
                         }, "wrong dict representation")

    def test_to_dict_with_id(self):
        instance = Rectangle(4, 8, 0, 0, 98)
        self.assertEqual(instance.to_dictionary(),
                         {
                             'id': 98,
                             'width': 4,
                             'height': 8,
                             'x': 0,
                             'y': 0
                         }, "wrong dict representation")

    def test_to_dict_with_all_args(self):
        instance = Rectangle(4, 8, 6, 9, 98)
        self.assertEqual(instance.to_dictionary(),
                         {
                             'id': 98,
                             'width': 4,
                             'height': 8,
                             'x': 6,
                             'y': 9
                         }, "wrong dict representation")

    def test_to_dict_after_update(self):
        instance = Rectangle(4, 8, 6, 9, 98)
        instance.update(id=99,
                        width=23,
                        height=35,
                        x=1,
                        y=2)
        self.assertEqual(instance.to_dictionary(),
                         {
                             'id': 99,
                             'width': 23,
                             'height': 35,
                             'x': 1,
                             'y': 2
                         }, "wrong dict representation")
