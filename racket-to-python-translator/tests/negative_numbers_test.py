import unittest
from ..main import test_line


class NegativeNumbersTest(unittest.TestCase):

    def test_basic_negative_number(self):
        self.assertEqual(test_line("(- 1)"), "-1")

    def test_basic_negative_number_with_sum(self):
        self.assertEqual(test_line("(- 1 2)"), "sub_all((1, 2))")

    def test_basic_negative_number_with_product(self):
        self.assertEqual(test_line("(* 1 -2)"), "mul_all((1, -2))")

    def test_basic_negative_number_with_divide(self):
        self.assertEqual(test_line("(/ 1 -2)"), "div_all((1, -2))")

    def test_basic_negative_number_with_minus(self):
        self.assertEqual(test_line("(- 1 -2)"), "sub_all((1, -2))")
