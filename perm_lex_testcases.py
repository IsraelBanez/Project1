import unittest
from perm_lex import*

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        """tests permutation for a string with a length of 2 """
        self.assertEqual(perm_gen_lex('ab'), ['ab','ba'])

    def test_perm_gen_lex1(self):
        """tests permutation for an empty string """
        self.assertEqual(perm_gen_lex(''), [])

    def test_perm_gen_lex2(self):
        """tests permutation for a string of numbers """
        self.assertEqual(perm_gen_lex('12'), ['12', '21'])

    def test_perm_gen_lex3(self):
        """tests permutation for a string with a length of 3 """
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex4(self):
        """tests permutation for None"""
        self.assertEqual(perm_gen_lex(None), None)

if __name__ == "__main__":
        unittest.main()
