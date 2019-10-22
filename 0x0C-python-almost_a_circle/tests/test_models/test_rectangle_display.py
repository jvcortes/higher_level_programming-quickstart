#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
"""
This module contains the unit tests for the `Base` class.
"""


class RectangleDisplayTest(unittest.TestCase):
    """
    Defines the test cases for the `Rectangle` class
    """

    @classmethod
    def setUpClass(cls):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_rectangle_display(self):
        output = StringIO()
        sys.stdout = output
        instance = Rectangle(4, 2)
        instance.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(),
                         "####\n"
                         "####",
                         "wrong output")

    def test_rectangle_display_big_rectangle(self):
        output = StringIO()
        sys.stdout = output
        instance = Rectangle(8, 8)
        instance.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(),
                         "########\n"
                         "########\n"
                         "########\n"
                         "########\n"
                         "########\n"
                         "########\n"
                         "########\n"
                         "########",
                         "wrong output")

    def test_rectangle_display_one_by_one_rectangle(self):
        output = StringIO()
        sys.stdout = output
        instance = Rectangle(1, 1)
        instance.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(),
                         "#",
                         "wrong output")
