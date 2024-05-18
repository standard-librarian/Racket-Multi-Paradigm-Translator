# test objectives
# test the basic operators for racket and that they are converted to python

import unittest
from ..main import test_line


class OperatorTest(unittest.TestCase):

    def test_basic_sum(self):
        self.assertEqual(test_line("(+ 1 2 3)"), "add_all((1, 2, 3))")

    def test_basic_product(self):
        self.assertEqual(test_line("(* 1 2 3)"), "mul_all((1, 2, 3))")

    def test_basic_divide(self):
        self.assertEqual(test_line("(/ 1 2 3)"), "div_all((1, 2, 3))")

    def test_basic_minus(self):
        self.assertEqual(test_line("(- 1 2 3)"), "sub_all((1, 2, 3))")

    def test_max(self):
        self.assertEqual(test_line("(max 3 2 4.1 2)"), "max(3, 2, 4.1, 2)")

    def test_min(self):
        self.assertEqual(test_line("(min 3 2 4.1 2)"), "min(3, 2, 4.1, 2)")
