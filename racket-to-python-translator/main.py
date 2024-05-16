import sys
import os

# SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(SCRIPT_DIR, "src"))


from .lexer import Lexer
from .parser import Parser


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
        with open(filename, "r") as file:
            for line in file:
                tokens = lexer.tokenize_line(line)
                parser = Parser(tokens)
                ast = parser.parse()
                if ast:
                    python_code = ast.generate_python_code()
                    print(python_code)
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


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
