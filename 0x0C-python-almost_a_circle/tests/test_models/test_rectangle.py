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

    def test_try_to_create_instance_with_width_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2.1, 2)

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_width_as_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("100", 2)

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_width_as_list(self):
        with self.assertRaises(TypeError) as context:
            Rectangle([10, 20], 2)

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_height_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 3.14)

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_height_as_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(100, "3")

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_height_as_list(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(20, [1, 2])

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_x_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 2, 1.0)

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_x_as_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 2, "1")

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_x_as_list(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(20, 2, [1])

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_y_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 2, 1, 12.3)

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_y_as_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 2, 1, "2")

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_y_as_list(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(20, 2, 1, [5, 2])

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_a_negative_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-2, 2)

        self.assertTrue('width must be > 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_a_zero_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)

        self.assertTrue('width must be > 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_a_negative_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(2, -2)

        self.assertTrue('height must be > 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_a_zero_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 0)

        self.assertTrue('height must be > 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_negative_x(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 5, -1)

        self.assertTrue('x must be >= 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_negative_y(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 5, 1, -1)

        self.assertTrue('y must be >= 0'
                        in str(context.exception))

    def test_set_instance_member_height(self):
        instance = Rectangle(2, 2)
        instance.height = 1
        self.assertEqual(instance.height, 1, "wrong height")

    def test_set_instance_member_height_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.height = "NUMBER"

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_set_instance_member_height_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.height = [1, 2]

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_set_instance_member_height_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.height = 2.2

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_set_instance_member_width(self):
        instance = Rectangle(2, 2)
        instance.width = 1
        self.assertEqual(instance.width, 1, "wrong width")

    def test_set_instance_member_width_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.width = "NUMBER"

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_set_instance_member_width_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.width = [1, 2]

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_set_instance_member_width_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.width = 2.2

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_set_instance_member_x(self):
        instance = Rectangle(2, 2)
        instance.x = 1
        self.assertEqual(instance.x, 1, "wrong x")

    def test_set_instance_member_x_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.x = "NUMBER"

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_set_instance_member_x_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.x = [1, 2]

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_set_instance_member_x_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.x = 2.2

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_set_instance_member_y(self):
        instance = Rectangle(2, 2)
        instance.y = 1
        self.assertEqual(instance.y, 1, "wrong y")

    def test_set_instance_member_y_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.y = "NUMBER"

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_set_instance_member_y_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.y = [1, 2]

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_set_instance_member_y_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Rectangle(2, 2)
            instance.y = 2.2

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_no_args(self):
        with self.assertRaises(TypeError) as context:
            Rectangle()

        self.assertTrue('__init__() missing 2 required positional arguments'
                        in str(context.exception))

    def test_try_to_create_instance_with_only_one_arg(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1)

        self.assertTrue('__init__() missing 1 required positional argument'
                        in str(context.exception))

    def test_try_to_create_instance_with_additional_args(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, 3, 4, 5, 6)

        self.assertTrue('__init__() takes from 3 to 6 positional arguments'
                        in str(context.exception))
