# test objectives
# test the basic operators for racket and that they are converted to python

import unittest
from ..main import test_line


class LambdaExpressionTest(unittest.TestCase):

    def test_basic_lambda_expression(self):
        self.assertEqual(test_line("(lambda (x) (+ x 1))"), "lambda x: add_all((x, 1))")

    def test_lambda_expression_with_multiple_parameters(self):
        self.assertEqual(
            test_line("(lambda (x y) (+ x y))"), "lambda x, y: add_all((x, y))"
        )

    def test_lambda_expression_with_multiple_expressions(self):
        self.assertEqual(
            test_line("(lambda (x y) (+ x y) (- x y))"),
            "lambda x, y: (add_all((x, y)), sub_all((x, y)))",
        )

    def test_lambda_expression_with_nested_expression(self):
        self.assertEqual(
            test_line("(lambda (x y) (+ x (- y 1)))"),
            "lambda x, y: add_all((x, sub_all((y, 1))))",
        )

    def test_lambda_with_no_parameters(self):
        self.assertEqual(test_line("(lambda () 1)"), "lambda : 1")

    def test_lambda_with_no_parameters_and_returning_string(self):
        self.assertEqual(test_line('(lambda () "hello")'), "lambda : 'hello'")
