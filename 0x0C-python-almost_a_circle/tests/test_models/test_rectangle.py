#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"""
This module contains the unit tests for the `Rectangle` class.
"""


class RectangleTest(unittest.TestCase):
    """
    Defines the test cases for the `Rectangle` class
    """

    @classmethod
    def setUpClass(cls):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_create_and_assert_instance(self):
        instance = Rectangle(3, 4)
        self.assertIsInstance(instance, Rectangle)

    def test_create_instance_with_only_required_args(self):
        instance = Rectangle(4, 2)
        self.assertEqual(instance.id, 2, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 2, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_create_instance_with_id(self):
        instance = Rectangle(5, 4, 0, 0, 98)
        self.assertEqual(instance.id, 98, "wrong id")
        self.assertEqual(instance.width, 5, "wrong width")
        self.assertEqual(instance.height, 4, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_create_instance_with_required_args_x_and_y_no_id(self):
        instance = Rectangle(5, 4, 0, 0)
        self.assertEqual(instance.id, 3, "wrong id")
        self.assertEqual(instance.width, 5, "wrong width")
        self.assertEqual(instance.height, 4, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_try_to_create_instance_with_no_args(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle()

        self.assertTrue('__init__() missing 2 required positional arguments'
                        in str(context.exception))

    def test_try_to_create_instance_with_only_one_arg(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(1)

        self.assertTrue('__init__() missing 1 required positional argument'
                        in str(context.exception))

    def test_try_to_create_instance_with_additional_args(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(1, 2, 3, 4, 5, 6)

        self.assertTrue('__init__() takes from 3 to 6 positional arguments'
                        in str(context.exception))
