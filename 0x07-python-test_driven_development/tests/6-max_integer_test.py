#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_end(self):
        self.assertEqual(max_integer([1, 2, 3 ,4 , 5]), 5)
    def test_max_integer_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)
    def test_max_integer_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
    def test_one_negative(self):
        self.assertEqual(max_integer([-1, 2, 3 ,4 ,5]), 5)
    def test_one_integer(self):
        self.assertEqual(max_integer([5]), 5)
    def test_empty(self):
        self.assertIsNone(max_integer[], None)

if __name__ == "__main__":
    unittest.main()
