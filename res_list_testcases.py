import unittest
from  rec_list import *

# Starter test cases - write more!

class TestRecList(unittest.TestCase):

    def test_first1(self):
        """tests for the lowest value near the end"""
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist), "49ers")

    def test_first2(self):
        """tests for None"""
        strlist = None
        self.assertEqual(first_string(strlist), None)

    def test_first3(self):
        """tests for the lowest value at the beginning """
        strlist = Node("369", Node("cuz", Node("bdd", None)))
        self.assertEqual(first_string(strlist), "369")

    def test_first4(self):
        """tests for the lowest value of all alpha strings only """
        strlist = Node("faker", Node("cuzz", Node("dbdd", None)))
        self.assertEqual(first_string(strlist), "cuzz")

    def test_split1(self):
        """tests for the order of strings with one of each category(vowel, consonant, and non-alpha """
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist), (Node('Abc', None), Node('xyz', None), Node('49ers', None)))

    def test_split2(self):
        """tests for the order of strings with two of each category(vowel, consonant, and non-alpha """
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist), (Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))

    def test_split3(self):
        """tests for None"""
        strlist = None
        self.assertEqual(split_list(strlist), (None, None, None))

if __name__ == "__main__":
        unittest.main()