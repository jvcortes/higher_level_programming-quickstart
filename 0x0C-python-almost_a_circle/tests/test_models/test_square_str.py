#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
"""
This module contains the unit tests for the `Square` class.
"""


class SquareStrTest(unittest.TestCase):
    """
    Defines the test cases for the `Square` class
    """

    def setUp(self):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_square_str_repr(self):
        instance = Square(4)
        self.assertEqual(str(instance), "[{}] (1) 0/0 - 4"
                         .format(instance.__class__.__name__))

    def test_square_str_repr_with_x_and_y(self):
        instance = Square(4, 4, 3)
        self.assertEqual(str(instance), "[{}] (1) 4/3 - 4"
                         .format(instance.__class__.__name__))

    def test_square_str_repr_with_x_y_and_id(self):
        instance = Square(4, 2, 8, 98)
        self.assertEqual(str(instance), "[{}] (98) 2/8 - 4"
                         .format(instance.__class__.__name__))
