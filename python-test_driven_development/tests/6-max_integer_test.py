#!/usr/bin/python3

import unittest
from your_module import max_integer  # Replace 'your_module' with the actual module name

class TestMaxInteger(unittest.TestCase):
    """Define test cases for max_integer function"""

    def test_max_at_end(self):
        """Test for the max integer at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test for the max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test for the max integer in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        """Test for a list with one element"""
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_with_negative_numbers(self):
        """Test for a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test for a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_equal(self):
        """Test for a list where all elements are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == "__main__":
    unittest.main()
