from token import Token
from token_types import TokenType

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


class Lexer:
    def __init__(self):
        self.tokens = []

    def advance(self):
        self.position += 1

    def peek(self):
        return self.code[self.position] if self.position < len(self.code) else ""

    def peek_next(self):
        return (
            self.code[self.position + 1] if self.position + 1 < len(self.code) else ""
        )

    def is_eof(self):
        return self.position >= len(self.code)

    def is_whitespace(self, char):
        return char in {" ", "\n", "\t"}

    def make_number(self):
        number = ""
        num_of_dots = 0
        while not self.is_eof() and self.peek().isdigit():
            number += self.peek()
            self.advance()
        if not self.is_eof() and self.peek() == ".":
            number += "."
            num_of_dots += 1
            self.advance()
            while not self.is_eof() and self.peek().isdigit():
                number += self.peek()
                self.advance()
        if num_of_dots == 0:
            return Token(TokenType.NUMBER, int(number))
        return Token(TokenType.NUMBER, float(number))

    def is_alpha(self, char):
        return char.isalpha()

    def is_alphanumeric(self, char):
        return char.isalnum()

    def tokenize_line(self, line):
        self.code = line
        self.position = 0
        self.tokens = []
        while not self.is_eof():
            char = self.peek()
            if self.is_whitespace(char):
                self.advance()
            elif char == "+":
                self.tokens.append(Token(TokenType.PLUS, char))
                self.advance()
            elif char == "-":
                self.tokens.append(Token(TokenType.MINUS, char))
                self.advance()
            elif char == "*":
                self.tokens.append(Token(TokenType.MULTIPLY, char))
                self.advance()
            elif char == "/":
                self.tokens.append(Token(TokenType.DIVIDE, char))
                self.advance()
            elif char == "%":
                self.tokens.append(Token(TokenType.MODULO, char))
                self.advance()
            elif char == "=":
                self.tokens.append(Token(TokenType.EQUAL, char))
                self.advance()
            elif char == "<":
                if self.peek_next() == "=":
                    self.tokens.append(Token(TokenType.LESS_EQUAL, "<="))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.LESS, char))
                    self.advance()
            elif char == ">":
                if self.peek_next() == "=":
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, ">="))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.GREATER, char))
                    self.advance()
            elif char == "(":
                self.tokens.append(Token(TokenType.LPAREN, char))
                self.advance()
            elif char == ")":
                self.tokens.append(Token(TokenType.RPAREN, char))
                self.advance()
            elif char == "{":
                self.tokens.append(Token(TokenType.LBRACE, char))
                self.advance()
            elif char == "}":
                self.tokens.append(Token(TokenType.RBRACE, char))
                self.advance()
            elif char == "[":
                self.tokens.append(Token(TokenType.LBRACKET, char))
                self.advance()
            elif char == "]":
                self.tokens.append(Token(TokenType.RBRACKET, char))
                self.advance()
            elif char == "'":
                self.tokens.append(Token(TokenType.QUOTE, char))
                self.advance()
            elif char == ".":
                self.tokens.append(Token(TokenType.DOT, char))
                self.advance()
            elif char == "#":
                self.advance()
                if self.peek() == "t":
                    self.tokens.append(Token(TokenType.BOOLEAN, True))
                    self.advance()
                elif self.peek() == "f":
                    self.tokens.append(Token(TokenType.BOOLEAN, False))
                    self.advance()
                elif self.peek() == "n":
                    self.tokens.append(Token(TokenType.NIL, None))
                    self.advance()
            elif char == ";":
                comment = ""
                while not self.is_eof() and self.peek() != "\n":
                    comment += self.peek()
                    self.advance()
                self.tokens.append(Token(TokenType.COMMENT, comment))
            elif char in digits:
                self.tokens.append(self.make_number())
            elif char.isalpha() or char == "?":
                identifier = ""
                while not self.is_eof() and (
                    self.is_alphanumeric(self.peek())
                    or self.peek() == "?"
                    or self.peek() == "_"
                    or self.peek() == "-"
                ):
                    identifier += self.peek()
                    self.advance()
                if identifier.upper() == "DEFINE":
                    self.tokens.append(Token(TokenType.DEFINE, identifier.upper()))
                elif identifier.upper() == "LET":
                    self.tokens.append(Token(TokenType.LET, identifier.upper()))
                elif identifier.upper() == "LAMBDA":
                    self.tokens.append(Token(TokenType.LAMBDA, identifier.upper()))
                elif identifier.upper() == "IF":
                    self.tokens.append(Token(TokenType.IF, identifier.upper()))
                elif identifier.upper() == "COND":
                    self.tokens.append(Token(TokenType.COND, identifier.upper()))
                elif identifier.upper() == "ELSE":
                    self.tokens.append(Token(TokenType.ELSE, identifier.upper()))
                elif identifier.upper() == "WHILE":
                    self.tokens.append(Token(TokenType.WHILE, identifier.upper()))
                elif identifier.upper() == "UNTIL":
                    self.tokens.append(Token(TokenType.UNTIL, identifier.upper()))
                elif identifier.upper() == "SET":
                    self.tokens.append(Token(TokenType.SET, identifier.upper()))
                elif identifier.upper() == "ZERO?":
                    self.tokens.append(Token(TokenType.ZERO_QMARK, identifier.upper()))
                elif identifier.upper() == "MAX":
                    self.tokens.append(Token(TokenType.MAX, identifier.upper()))
                elif identifier.upper() == "SQRT":
                    self.tokens.append(Token(TokenType.SQRT, identifier.upper()))
                elif identifier.upper() == "MAP":
                    self.tokens.append(Token(TokenType.MAP, identifier.upper()))
                elif identifier.upper() == "FOLDL":
                    self.tokens.append(Token(TokenType.FOLDL, identifier.upper()))
                elif identifier.upper() == "WRITELN":
                    self.tokens.append(Token(TokenType.WRITELN, identifier.upper()))
                elif identifier.upper() == "LIST":
                    self.tokens.append(Token(TokenType.LIST, identifier.upper()))

                else:
                    self.tokens.append(Token(TokenType.IDENTIFIER, identifier))
                identifier = ""
            elif char == '"':
                string = ""
                self.advance()
                while not self.is_eof() and self.peek() != '"':
                    string += self.peek()
                    self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.STRING, string))
            else:
                self.advance()
        return self.tokens