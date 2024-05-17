import sys
import os

from .lexer import Lexer
from .parser import Parser
from .parse_tree_printer import print_parse_tree


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
