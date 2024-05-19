# test objectives
# test the basic operators for racket and that they are converted to python

import unittest
from ..main import test_line


class VariableDefintionTest(unittest.TestCase):

    def test_basic_variable_definition(self):
        self.assertEqual(test_line("(define a 1)"), "a = 1")

    def test_basic_variable_definition_with_string(self):
        self.assertEqual(test_line('(define a "hello")'), 'a = "hello"')

    def test_basic_variable_definition_with_list(self):
        self.assertEqual(test_line("(define a (list 1 2 3))"), "a = list((1, 2, 3))")

    def test_basic_variable_definition_with_list_of_strings(self):
        self.assertEqual(
            test_line('(define a (list "hello" "world"))'),
            'a = list(("hello", "world"))',
        )

    def test_basic_variable_definition_with_list_of_lists(self):
        self.assertEqual(
            test_line("(define a (list (list 1 2) (list 3 4)))"),
            "a = list((list((1, 2)), list((3, 4))))",
        )

    def test_basic_variable_definition_with_list_of_lists_of_strings(self):
        self.assertEqual(
            test_line(
                '(define a (list (list "hello" "world") (list "goodbye" "world")))'
            ),
            'a = list((list(("hello", "world")), list(("goodbye", "world"))))',
        )
