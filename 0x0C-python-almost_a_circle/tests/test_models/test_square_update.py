#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
"""
This module contains the unit tests for the `Square` class.
"""


class SquareUpdateTest(unittest.TestCase):
    """
    Defines the test cases for the `Squre` class
    """

    def setUp(self):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_square_update_id(self):
        instance = Square(4)
        instance.update(420)
        self.assertEqual(instance.id, 420, "wrong id")

    def test_square_update_size(self):
        instance = Square(4)
        instance.update(instance.id, 8)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 8, "wrong size")

    def test_square_update_x(self):
        instance = Square(4, 9)
        instance.update(instance.id, instance.size, 5)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 4, "wrong size")
        self.assertEqual(instance.x, 5, "wrong x")

    def test_square_update_y(self):
        instance = Square(4, 9, 2)
        instance.update(instance.id,
                        instance.size,
                        instance.x,
                        21)

        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 4, "wrong size")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 21, "wrong y")

    def test_square_update_all(self):
        instance = Square(4, 2, 23, 10)
        instance.update(100,
                        7,
                        7,
                        9)

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.size, 7, "wrong size")
        self.assertEqual(instance.x, 7, "wrong x")
        self.assertEqual(instance.y, 9, "wrong y")

    def test_square_update_no_args(self):
        instance = Square(4, 2, 23)
        instance.update()

        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 4, "wrong size")
        self.assertEqual(instance.x, 2, "wrong x")
        self.assertEqual(instance.y, 23, "wrong y")

    def test_square_update_additional_args(self):
        instance = Square(4, 2, 23, 10)
        instance.update(100,
                        7,
                        7,
                        9,
                        "additional argument",
                        88)

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.size, 7, "wrong size")
        self.assertEqual(instance.x, 7, "wrong x")
        self.assertEqual(instance.y, 9, "wrong y")

    def test_square_update_negative_size(self):
        instance = Square(4, 2, 23, 10)
        with self.assertRaises(ValueError) as context:

            instance.update(100,
                            -7,
                            7,
                            9)

            self.assertTrue("width must be > 0" in str(context.exception))

    def test_square_update_zero_size(self):
        instance = Square(4, 2, 23, 10)
        with self.assertRaises(ValueError) as context:

            instance.update(100,
                            0,
                            7,
                            9)

            self.assertTrue("width must be > 0" in str(context.exception))

    def test_square_update_negative_negative_x(self):
        instance = Square(4, 2, 23, 10)
        with self.assertRaises(ValueError) as context:

            instance.update(100,
                            0,
                            -3,
                            0)

            self.assertTrue("x must be >= 0" in str(context.exception))

    def test_square_update_kwarg_id(self):
        instance = Square(4)
        instance.update(id=420)
        self.assertEqual(instance.id, 420, "wrong id")

    def test_square_update_kwarg_size(self):
        instance = Square(4)
        instance.update(size=8)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 8, "wrong size")

    def test_square_update_kwarg_x(self):
        instance = Square(4, 2)
        instance.update(x=5)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 4, "wrong size")
        self.assertEqual(instance.x, 5, "wrong x")

    def test_square_update_kwarg_y(self):
        instance = Square(4, 2, 4)
        instance.update(y=7)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.size, 4, "wrong size")
        self.assertEqual(instance.x, 2, "wrong x")
        self.assertEqual(instance.y, 7, "wrong y")

    def test_square_update_kwarg_all(self):
        instance = Square(4, 2, 23, 10)
        instance.update(id=100,
                        size=7,
                        x=9,
                        y=0)

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.size, 7, "wrong size")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_square_update_args_and_kwargs(self):
        instance = Square(4, 2, 23, 10)
        instance.update(68,
                        id=100,
                        size=7,
                        x=9,
                        y=0)

        self.assertEqual(instance.id, 68, "wrong id")
        self.assertEqual(instance.size, 4, "wrong size")
        self.assertEqual(instance.x, 2, "wrong x")
        self.assertEqual(instance.y, 23, "wrong y")

    def test_square_update_additional_kwargs(self):
        instance = Square(4, 2, 23, 10)
        instance.update(id=100,
                        size=7,
                        x=9,
                        y=0,
                        additional="argument")

        self.assertEqual(instance.id, 100, "wrong id")
        self.assertEqual(instance.size, 7, "wrong size")
        self.assertEqual(instance.x, 9, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_square_update_kwarg_negative_size(self):
        instance = Square(4, 2, 23, 10)
        with self.assertRaises(ValueError) as context:
            instance.update(id=100,
                            size=-7,
                            x=9,
                            y=2,
                            additional="argument")

        self.assertTrue("width must be > 0" in str(context.exception))

    def test_square_update_kwarg_negative_x(self):
        instance = Square(4, 2, 23, 10)
        with self.assertRaises(ValueError) as context:
            instance.update(id=100,
                            size=7,
                            x=-9,
                            additional="argument")

        self.assertTrue("x must be >= 0" in str(context.exception))
