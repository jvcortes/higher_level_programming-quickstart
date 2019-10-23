#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
"""
This module contains the unit tests for the `Square` class.
"""


class SquareTest(unittest.TestCase):
    """
    Defines the test cases for the `Square` class
    """

    def setUp(self):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_create_and_assert_instance(self):
        instance = Square(3)
        self.assertIsInstance(instance, Square)
        self.assertIsInstance(instance, Rectangle)

    def test_create_instance_with_only_required_args(self):
        instance = Square(4)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 4, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_create_instance_with_id(self):
        instance = Square(4, 0, 0, 98)
        self.assertEqual(instance.id, 98, "wrong id")
        self.assertEqual(instance.width, 4, "wrong width")
        self.assertEqual(instance.height, 4, "wrong height")
        self.assertEqual(instance.x, 0, "wrong x")
        self.assertEqual(instance.y, 0, "wrong y")

    def test_create_instance_with_required_args_x_and_y_no_id(self):
        instance = Square(5, 4, 2)
        self.assertEqual(instance.id, 1, "wrong id")
        self.assertEqual(instance.width, 5, "wrong width")
        self.assertEqual(instance.height, 5, "wrong height")
        self.assertEqual(instance.x, 4, "wrong x")
        self.assertEqual(instance.y, 2, "wrong y")

    def test_try_to_create_instance_with_size_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Square(2.1)

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_size_as_string(self):
        with self.assertRaises(TypeError) as context:
            Square("100")

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_size_as_list(self):
        with self.assertRaises(TypeError) as context:
            Square([10, 20], 2)

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_x_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Square(2, 1.0)

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_x_as_string(self):
        with self.assertRaises(TypeError) as context:
            Square(2, "1")

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_x_as_list(self):
        with self.assertRaises(TypeError) as context:
            Square(20, [1])

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_y_as_floating_point(self):
        with self.assertRaises(TypeError) as context:
            Square(2, 2, 12.3)

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_y_as_string(self):
        with self.assertRaises(TypeError) as context:
            Square(2, 1, "2")

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_y_as_list(self):
        with self.assertRaises(TypeError) as context:
            Square(20, 1, [5, 2])

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_a_negative_size(self):
        with self.assertRaises(ValueError) as context:
            Square(-2)

        self.assertTrue('width must be > 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_a_zero_size(self):
        with self.assertRaises(ValueError) as context:
            Square(0)

        self.assertTrue('width must be > 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_negative_x(self):
        with self.assertRaises(ValueError) as context:
            Square(5, -1)

        self.assertTrue('x must be >= 0'
                        in str(context.exception))

    def test_try_to_create_instance_with_negative_y(self):
        with self.assertRaises(ValueError) as context:
            Square(2, 5, -1)

        self.assertTrue('y must be >= 0'
                        in str(context.exception))

    def test_set_instance_member_height(self):
        instance = Square(8)
        instance.height = 6
        self.assertEqual(instance.height, 6, "wrong height")

    def test_set_instance_member_height_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.height = "NUMBER"

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_set_instance_member_height_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.height = [1, 2]

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_set_instance_member_height_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.height = 2.2

        self.assertTrue('height must be an integer'
                        in str(context.exception))

    def test_set_instance_member_width(self):
        instance = Square(2)
        instance.width = 1
        self.assertEqual(instance.width, 1, "wrong width")

    def test_set_instance_member_width_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.width = "NUMBER"

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_set_instance_member_width_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.width = [1, 2]

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_set_instance_member_width_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.width = 2.2

        self.assertTrue('width must be an integer'
                        in str(context.exception))

    def test_set_instance_member_x(self):
        instance = Square(2)
        instance.x = 1
        self.assertEqual(instance.x, 1, "wrong x")

    def test_set_instance_member_x_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.x = "NUMBER"

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_set_instance_member_x_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.x = [1, 2]

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_set_instance_member_x_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.x = 2.2

        self.assertTrue('x must be an integer'
                        in str(context.exception))

    def test_set_instance_member_y(self):
        instance = Square(2)
        instance.y = 1
        self.assertEqual(instance.y, 1, "wrong y")

    def test_set_instance_member_y_to_string(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.y = "NUMBER"

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_set_instance_member_y_to_list(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.y = [1, 2]

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_set_instance_member_y_to_float(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(2)
            instance.y = 2.2

        self.assertTrue('y must be an integer'
                        in str(context.exception))

    def test_try_to_create_instance_with_no_args(self):
        with self.assertRaises(TypeError) as context:
            Square()

        self.assertTrue('__init__() missing 1 required positional argument:'
                        ' \'size\''
                        in str(context.exception))

    def test_try_to_create_instance_with_additional_args(self):
        with self.assertRaises(TypeError) as context:
            Square(1, 2, 3, 4, 5, 6)

        self.assertTrue('__init__() takes from 2 to 5 positional arguments'
                        in str(context.exception))

    def test_set_size(self):
        instance = Square(4)
        instance.size = 3
        self.assertEqual(instance.size, 3, "wrong size")

    def test_set_negative_size(self):
        with self.assertRaises(ValueError) as context:
            instance = Square(4)
            instance.size = -3

        self.assertTrue('width must be > 0' in str(context.exception))

    def test_set_zero_size(self):
        with self.assertRaises(ValueError) as context:
            instance = Square(4)
            instance.size = 0

        self.assertTrue('width must be > 0' in str(context.exception))

    def test_set_non_int_size(self):
        with self.assertRaises(TypeError) as context:
            instance = Square(4)
            instance.size = 8.23

        self.assertTrue('width must be an integer' in str(context.exception))
