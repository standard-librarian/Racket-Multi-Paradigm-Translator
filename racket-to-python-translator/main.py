import sys
import os

from .lexer import Lexer
from .parser import Parser
from .parse_tree_printer import print_parse_tree


def test_multiple_lines(racket_lines: list):
    lexer = Lexer()
    python_code = ""
    for line in racket_lines:
        python_code += test_line(line) + "\n"
    return python_code


def test_line(racket_line: str):
    lexer = Lexer()
    tokens = lexer.tokenize_line(racket_line)
    parser = Parser(tokens)
    ast = parser.parse()
    python_code = None
    if ast:
        python_code = ast.generate_python_code()
    return python_code


def main(filename=None):
    lexer = Lexer()
    if filename:
        with open("parse_tree.txt", "w") as file:
            file.write("")
        with open("output_code.py", "w") as file:
            file.write("")

        with open("output_code.py", "a") as file:
            file.write(
                """
from functools import reduce
import operator
from math import sqrt
binary_func_all = lambda func: lambda l: reduce(func, l)
add_all = binary_func_all(operator.add) # +
sub_all = binary_func_all(operator.sub) # -
mul_all = binary_func_all(operator.mul) # *
div_all = binary_func_all(operator.truediv) # /

all_binary_func = lambda func: lambda l: all([True if func(l[i -1], l[i]) else False for i in range(1, len(l))])
all_eq = all_binary_func(operator.eq) # ==
all_gt = all_binary_func(operator.gt) # >
all_ge = all_binary_func(operator.ge) # >=
all_lt = all_binary_func(operator.lt) # <
all_le = all_binary_func(operator.le) # <=

"""
            )

        with open(filename, "r") as file:
            for line in file:
                tokens = lexer.tokenize_line(line)
                parser = Parser(tokens)
                ast = parser.parse()
                if ast:
                    python_code = ast.generate_python_code()
                    tree = print_parse_tree(ast)
                    with open("output_code.py", "a") as file:
                        file.write(python_code + "\n")
                    with open("parse_tree.txt", "a") as file:
                        file.write("\n" + line + "\n" + tree)
                        file.write(
                            "*******************************************************"
                        )

    else:
        while True:
            text = input("racket >> ")
            if text == "exit":
                break
            tokens = lexer.tokenize_line(text)
            # print ("tokens = " , tokens)
            parser = Parser(tokens)
            ast = parser.parse()
            if ast:
                python_code = ast.generate_python_code()
                print(python_code)
                print(print_parse_tree(ast))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
