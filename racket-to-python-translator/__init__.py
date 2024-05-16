from sys import path
from os import path as ospath

path.append("racket-to-python-translator")
path.append("racket-to-python-translator/lexer")
path.append("racket-to-python-translator/parser")


from .main import test_line
from .lexer import Lexer


__all__ = ["test_line", "Lexer"]
