#!/usr/bin/python3
import unittest
"""
This module contains the unit tests for the `Base` class.
"""


class BaseTest(unittest.TestCase):
    """
    Defines the test cases for the `Base` class
    """

    def setUp(self):
        self.Base = __import__("models/0-base").Base

    def test_assert_instance(self):
        instance = self.Base()
        self.assertIsInstance(instance, self.Base)

    def test_create_instance_with_no_args(self):
        instance = self.Base()
        self.assertEqual(instance.id, 1, "wrong id")

    def test_create_instance_with_id(self):
        instance = self.Base(98)
        self.assertEqual(instance.id, 98, "wrong id")
