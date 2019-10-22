#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"""
This module contains the unit tests for the `Rectangle` class.
"""


class RectangleStrTest(unittest.TestCase):
    """
    Defines the test cases for the `Rectangle` class
    """

    @classmethod
    def setUpClass(cls):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_rectangle_str_repr(self):
        instance = Rectangle(4, 2)
        self.assertEqual(str(instance), "[{}] (1) 0/0 - 4/2"
                         .format(instance.__class__.__name__))

    def test_rectangle_str_repr_with_x_and_y(self):
        instance = Rectangle(4, 2, 8, 2)
        self.assertEqual(str(instance), "[{}] (2) 8/2 - 4/2"
                         .format(instance.__class__.__name__))

    def test_rectangle_str_repr_with_x_y_and_id(self):
        instance = Rectangle(4, 2, 8, 2, 98)
        self.assertEqual(str(instance), "[{}] (98) 8/2 - 4/2"
                         .format(instance.__class__.__name__))
