#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""
This module contains the unit tests for the `Base` class.
"""


class RectangleUpdateTest(unittest.TestCase):
    """
    Defines the test cases for the `Base` class
    """

    def setUp(self):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_rectangle_update_id(self):
        instance = Rectangle(4, 2)
        instance.update(420)
        self.assertEqual(instance.id, 420, "wrong id")

    def test_rectangle_update_width(self):
        instance = Rectangle(4, 2)
        instance.update(instance.id, 8)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 8, "wrong width")

    def test_rectangle_update_height(self):
        instance = Rectangle(4, 2)
        instance.update(instance.id, instance.width, 7)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 7, "wrong height")

    def test_rectangle_update_x(self):
        instance = Rectangle(4, 2)
        instance.update(instance.id, instance.width, instance.height, 5)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 5, "wrong x")

    def test_rectangle_update_y(self):
        instance = Rectangle(4, 2)
        instance.update(instance.id,
                        instance.width,
                        instance.height,
                        instance.x,
                        7)

        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 7, "wrong y")

    def test_rectangle_update_all(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        instance.update(100,
                        7,
                        7,
                        9,
                        0)

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.width, 7, "wrong width")
        self.assertEqual(instance.height, 7, "wrong height")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_rectangle_update_no_args(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        instance.update()

        self.assertEqual(instance.id, 96, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 23, "wrong x")
        self.assertEqual(instance.y, 10, "wrong y")

    def test_rectangle_update_additional_args(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        instance.update(100,
                        7,
                        7,
                        9,
                        0,
                        "additional argument",
                        88)

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.width, 7, "wrong width")
        self.assertEqual(instance.height, 7, "wrong height")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_rectangle_update_negative_width(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        with self.assertRaises(ValueError) as context:

            instance.update(100,
                            -7,
                            7,
                            9,
                            0)

            self.assertTrue("width must be > 0" in str(context.exception))

    def test_rectangle_update_zero_width(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        with self.assertRaises(ValueError) as context:

            instance.update(100,
                            0,
                            7,
                            9,
                            0)

            self.assertTrue("width must be > 0" in str(context.exception))

    def test_rectangle_update_negative_negative_x(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        with self.assertRaises(ValueError) as context:

            instance.update(100,
                            0,
                            7,
                            -3,
                            0)

            self.assertTrue("x must be >= 0" in str(context.exception))

    def test_rectangle_update_kwarg_id(self):
        instance = Rectangle(4, 2)
        instance.update(id=420)
        self.assertEqual(instance.id, 420, "wrong id")

    def test_rectangle_update_kwarg_width(self):
        instance = Rectangle(4, 2)
        instance.update(width=8)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 8, "wrong width")

    def test_rectangle_update_kwarg_height(self):
        instance = Rectangle(4, 2)
        instance.update(height=7)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 7, "wrong height")

    def test_rectangle_update_kwarg_x(self):
        instance = Rectangle(4, 2)
        instance.update(x=5)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 5, "wrong x")

    def test_rectangle_update_kwarg_y(self):
        instance = Rectangle(4, 2)
        instance.update(y=7)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 7, "wrong y")

    def test_rectangle_update_kwarg_all(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        instance.update(id=100,
                        width=7,
                        height=7,
                        x=9,
                        y=0)

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.width, 7, "wrong width")
        self.assertEqual(instance.height, 7, "wrong height")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_rectangle_update_args_and_kwargs(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        instance.update(68,
                        id=100,
                        width=7,
                        height=7,
                        x=9,
                        y=0)

        self.assertEqual(instance.id, 68, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 23, "wrong x")
        self.assertEqual(instance.y, 10, "wrong y")

    def test_rectangle_update_additional_kwargs(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        instance.update(id=100,
                        width=7,
                        height=7,
                        x=9,
                        y=0,
                        additional="argument")

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.width, 7, "wrong width")
        self.assertEqual(instance.height, 7, "wrong height")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_rectangle_update_kwarg_negative_width(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        with self.assertRaises(ValueError) as context:
            instance.update(id=100,
                            width=-7,
                            height=7,
                            x=9,
                            y=0,
                            additional="argument")

        self.assertTrue("width must be > 0" in str(context.exception))

    def test_rectangle_update_kwarg_negative_x(self):
        instance = Rectangle(4, 2, 23, 10, 96)
        with self.assertRaises(ValueError) as context:
            instance.update(id=100,
                            width=7,
                            height=7,
                            x=-9,
                            y=0,
                            additional="argument")

        self.assertTrue("x must be >= 0" in str(context.exception))
