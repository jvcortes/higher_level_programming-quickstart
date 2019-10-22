#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""
This module contains the unit tests for the `Base` class.
"""


class RectangleAreaTest(unittest.TestCase):
    """
    Defines the test cases for the `Base` class
    """

    @classmethod
    def setUpClass(cls):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_area(self):
        instance = Rectangle(4, 5)
        self.assertEqual(instance.area(), 20)

    def test_area_big_number(self):
        instance = Rectangle(4444444444444444444444, 1111111111111111111111111)
        self.assertEqual(instance.area(), 4444444444444444444444 *
                         1111111111111111111111111)

    def test_area_args(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(1, 4)
            instance.area(1)

        self.assertTrue('area() takes 1 positional argument but 2 were given'
                        in str(context.exception))
