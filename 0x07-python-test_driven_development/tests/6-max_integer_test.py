import unittest
"""
This module contains the unit tests for task 5.
"""


class MaxIntegerTestCase(unittest.TestCase):
    """
    Defines the test cases for the function max_integer
    """

    def setUp(self):
        self.max_integer = __import__("6-max_integer").max_integer

    def test_int(self):
        li = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        self.assertEqual(self.max_integer(li), 30, 'wrong max integer')

    def test_empty(self):
        self.assertEqual(self.max_integer([]), None, 'the list is not empty')

    def test_equals(self):
        li = [24, 24, 24, 24, 24, 24, 24, 24, 24, 24]
        self.assertEqual(self.max_integer(li), 24, 'wrong max integer')

    def test_negative(self):
        li = [-23, -44, -10, -3]
        self.assertEqual(self.max_integer(li), -3, 'wrong max integer')

    def test_negative_mixed(self):
        li = [-23, 44, 10, -3, 0, 28]
        self.assertEqual(self.max_integer(li), 44, 'wrong max integer')

    def test_one_value(self):
        li = [38]
        self.assertEqual(self.max_integer(li), 38, 'wrong max integer')

    def test_max_beginning(self):
        li = [10, 9, 5, 4, 0]
        self.assertEqual(self.max_integer(li), 10, 'wrong max integer')

    def test_max_middle(self):
        li = [2, 4, 6, 8, 10, 8, 6, 4, 2]
        self.assertEqual(self.max_integer(li), 10, 'wrong max integer')
