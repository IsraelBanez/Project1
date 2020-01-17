import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    """tests for an n value of 250"""
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        """tests for an n value at 42"""
        self.assertTrue(bears(42))

    def test_bear_03(self):
        """tests for an n value that meets none of the 3 conditions"""
        self.assertFalse(bears(53))

    def test_bear_04(self):
        """tests for an n value below 42"""
        self.assertFalse(bears(41))

    def test_bear_05(self):
        """tests for an n thats a negative"""
        self.assertFalse(bears(-1))

    def test_bear_06(self):
        """tests for an n value of None"""
        self.assertFalse(bears(None))

if __name__ == "__main__":
    unittest.main()
