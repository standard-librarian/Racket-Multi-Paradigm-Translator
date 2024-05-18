# test objectives
# test the basic operators for racket and that they are converted to python

import unittest
from ..main import test_line


class CommentsTest(unittest.TestCase):

    def test_basic_comment(self):
        self.assertEqual(test_line("; testing comment"), "# testing comment")
