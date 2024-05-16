from enum import Enum


class TokenType(Enum):
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    LBRACKET = "["
    RBRACKET = "]"
    QUOTE = "'"
    STRING = "STRING"
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    BOOLEAN = "BOOLEAN"
    NIL = "NIL"
    DOT = "."
    EOF = "EOF"
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"
    EQUAL = "="
    LESS = "<"
    GREATER = ">"
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="
    NOT_EQUAL = "!="
    DEFINE = "DEFINE"
    LET = "LET*"
    LAMBDA = "LAMBDA"
    IF = "IF"
    COND = "COND"
    WHILE = "WHILE"
    UNTIL = "UNTIL"
    SET = "SET"
    ZERO_QMARK = "ZERO_QMARK"
    ELSE = "ELSE"
    COMMENT = "COMMENT"
    MAX = "MAX"
    SQRT = "SQRT"
    MAP = "MAP"
    FOLDL = "FOLDL"
    WRITELN = "WRITELN"
    LIST = "LIST"


class IdentifierType(Enum):
    FUNCTION = "FUNCTION"
    VARIABLE = "VARIABLE"
