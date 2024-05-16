import sys

from lexar import Lexer
from parser import Parser


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
