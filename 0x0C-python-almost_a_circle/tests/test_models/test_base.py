#!/usr/bin/python3
import unittest
from models.base import Base
"""
This module contains the unit tests for the `Base` class.
"""


class BaseTest(unittest.TestCase):
    """
    Defines the test cases for the `Base` class
    """

    @classmethod
    def setUpClass(cls):
        for name in Base.__dict__:
            if "__nb_objects" in name:
                setattr(Base, name, 0)

    def test_create_and_assert_instance(self):
        instance = Base()
        self.assertIsInstance(instance, Base)

    def test_create_another_instance_with_no_args(self):
        instance = Base()
        self.assertEqual(instance.id, 2, "wrong id")

    def test_create_instance_with_id(self):
        instance = Base(98)
        self.assertEqual(instance.id, 98, "wrong id")
