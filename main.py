from enum import Enum

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

user_defined_identifiers = {}


class IdentifierType(Enum):
    FUNCTION = "FUNCTION"
    VARIABLE = "VARIABLE"


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


class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, '{self.value}')"

    def __repr__(self):
        return self.__str__()


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


class ASTNode:
    def generate_python_code(self):
        pass


class DisplayNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

    def generate_python_code(self):
        return f"print({self.expr.generate_python_code()})"

class IdentifierNode(ASTNode):
    def __init__(self, token):
        self.token = token

    def generate_python_code(self):
        return self.token.value

    def __str__(self):
        return self.token.value

    def __repr__(self):
        return self.__str__()


class FunctionCallNodeWithOperands(ASTNode):
    def __init__(self, token, operands):
        self.token = token
        self.operands = operands

    def generate_python_code(self):
        output = f"{self.token.value}("
        for operand in self.operands:
            output += f"{operand.generate_python_code()}, "
        output = output[:-2]
        output += ")"
        return output

    def __str__(self):
        return self.token.value

    def __repr__(self):
        return self.__str__()


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def generate_python_code(self):
        return str(self.value)


class DefineNode(ASTNode):
    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr

    def generate_python_code(self):
        return f"{self.identifier.generate_python_code()} = {self.expr.generate_python_code()}"


class ListNodes(ASTNode):
    def __init__(self, elements):
        self.elements = elements

    def generate_python_code(self):
        return f"list(({', '.join([element.generate_python_code() for element in self.elements])}))"
    

class LetDefinitionNode(ASTNode):
    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr

    def generate_python_code(self):
        return f"{self.identifier.generate_python_code()} = {self.expr.generate_python_code()}"

    def __str__(self):
        return f"LetDefinitionNode({self.identifier}, {self.expr})"

    def __repr__(self):
        return self.__str__()



class LetDefinitionNode(ASTNode):
    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr

    def generate_python_code(self):
        return f"{self.identifier.generate_python_code()} = {self.expr.generate_python_code()}"

    def __str__(self):
        return f"LetDefinitionNode({self.identifier}, {self.expr})"

    def __repr__(self):
        return self.__str__()


class LetNode(ASTNode):
    def __init__(self, bindings, expr):
        self.bindings = bindings
        self.expr = expr

    def generate_python_code(self):
        bindings_str = ", ".join(
            [
                f"{identifier.generate_python_code()} = {value.generate_python_code()}"
                for identifier, value in self.bindings
            ]
        )
        "(lambda x=3, y=x+1: print(x, y)) ()"

        return f"(lambda {bindings_str}: {self.expr.generate_python_code()})()"
    def __str__(self):
        return f"LetDefinitionNode({self.identifier}, {self.expr})"

    def __repr__(self):
        return self.__str__()


class LambdaNode(ASTNode):
    def __init__(self, params, expr):
        self.params = params
        self.expr = expr

    def generate_python_code(self):
        params_str = ", ".join([param.generate_python_code() for param in self.params])
        return f"lambda {params_str}: {self.expr.generate_python_code()}"

    def __str__(self):
        return f"LambdaNode({self.params}, {self.expr})"

    def __repr__(self):
        return self.__str__()


class MULTNode(ASTNode):
    def __init__(self, operands):
        self.operands = operands

    def generate_python_code(self):
        # mul_all((2, 5, 7))
        output = "mul_all(("
        for operand in self.operands:
            if isinstance(operand, NumberNode):
                output += f"{operand.value}, "
            else:
                output += operand.generate_python_code() + ", "
        output = output[:-2]
        output += "))"
        return output

    def __str__(self):
        return f"MULTNode({self.operands})"

    def __repr__(self):
        return self.__str__()


class AddNode(ASTNode):
    def __init__(self, operands):
        self.operands = operands
    def generate_python_code(self):
        # add_all((2, 5, 7))
        output = "add_all(("
        for operand in self.operands:
            if isinstance(operand, NumberNode):
                output += f"{operand.value}, "
            else:
                output += operand.generate_python_code() + ", "

        output = output[:-2]
        output += "))"
        return output

    def __str__(self):
        return f"AddNode({self.operands})"

    def __repr__(self):
        return self.__str__()


class SubNode(ASTNode):
    def __init__(self, operands):
        self.operands = operands

    def generate_python_code(self):
        # sub_all((2, 5, 7))
        output = "sub_all(("
        for operand in self.operands:
            if isinstance(operand, NumberNode):
                output += f"{operand.value}, "
            else:
                output += operand.generate_python_code() + ", "

        output = output[:-2]
        output += "))"
        return output

    def __str__(self):
        return f"SubNode({self.operands})"

    def __repr__(self):
        return self.__str__()


class DivNode(ASTNode):
    def __init__(self, operands):
        self.operands = operands

    def generate_python_code(self):
        # div_all((2, 5, 7))
        output = "div_all(("
        for operand in self.operands:
            if isinstance(operand, NumberNode):
                output += f"{operand.value}, "
            else:
                output += operand.generate_python_code() + ", "
        output = output[:-2]
        output += "))"
        return output

    def __str__(self):
        return f"DivNode({self.operands})"

    def __repr__(self):
        return self.__str__()


class IfNode(ASTNode):
    def __init__(self, condition, true_branch, false_branch=None):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def generate_python_code(self):
        if self.false_branch:
            return f"({self.true_branch.generate_python_code()} if {self.condition.generate_python_code()} else {self.false_branch.generate_python_code()})"
        else:
            return f"({self.true_branch.generate_python_code()} if {self.condition.generate_python_code()} else None)"


class CondNode(ASTNode):
    def __init__(self, cases):
        self.cases = cases

    def generate_python_code(self):
        return f"({next((expr.generate_python_code() for cond, expr in self.cases if cond), None)})"

class EqualNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def generate_python_code(self):
        return f"({self.left.generate_python_code()} == {self.right.generate_python_code()})"

class StringNode(ASTNode):
    def __init__(self, token):
        self.token = token

    def generate_python_code(self):
        return repr(self.token.value)


class IfNode(ASTNode):
    def __init__(self, condition, true_branch, false_branch=None):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def generate_python_code(self):
        if self.false_branch:
            return f"({self.true_branch.generate_python_code()} if {self.condition.generate_python_code()} else {self.false_branch.generate_python_code()})"
        else:
            return f"({self.true_branch.generate_python_code()} if {self.condition.generate_python_code()} else None)"


class CondNode(ASTNode):
    def __init__(self, cases):
        self.cases = cases

    def generate_python_code(self):
        return f"({next((expr.generate_python_code() for cond, expr in self.cases if cond), None)})"

class EqualNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def generate_python_code(self):
        return f"({self.left.generate_python_code()} == {self.right.generate_python_code()})"



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def peek(self):
        return self.tokens[self.tok_idx + 1]

    def parse(self):
        return self.expr()


    def expr(self):
        tok_type = self.current_tok.type
        if tok_type == TokenType.IDENTIFIER:
            return self.identifier_expr()
        elif self.current_tok.type == TokenType.STRING:
            token = self.current_tok
            self.advance()
            return StringNode(token)
        elif tok_type == TokenType.LPAREN:
            return self.group_expr()
        elif tok_type == TokenType.NUMBER:
            return self.number_expr()
        elif tok_type == TokenType.DEFINE:
            return self.define_expr()
        elif tok_type == TokenType.LET:
            return self.let_expr()
        elif tok_type == TokenType.LAMBDA:
            return self.lambda_expr()
        elif tok_type == TokenType.PLUS:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                expr = self.expr()
                operands.append(expr)
            return AddNode(operands)
        elif tok_type == TokenType.IF:
            return self.if_expr()
        elif tok_type == TokenType.COND:
            return self.cond_expr()
        elif tok_type == TokenType.MINUS:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                operands.append(self.expr())
            return SubNode(operands)
        elif tok_type == TokenType.MULTIPLY:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                operands.append(self.expr())
            return MULTNode(operands)
        elif tok_type == TokenType.DIVIDE:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                operands.append(self.expr())
            return DivNode(operands)
        elif tok_type == TokenType.EQUAL:
            self.advance()
            left = self.expr()
            right = self.expr()
            return EqualNode(left, right)
        elif tok_type == TokenType.NUMBER:
            return self.number_expr()
        elif tok_type == TokenType.LIST:
            return self.list_expr()
        else:
            # Handle syntax errors or unsupported expressions
            pass


    def identifier_expr(self):
        token = self.current_tok
        self.advance()

        if token.value == "display":
            self.advance()
            expr = self.expr()
            return DisplayNode(expr)
        if token.value in user_defined_identifiers:
            identifier_type, value = user_defined_identifiers[token.value]
            if identifier_type == IdentifierType.FUNCTION:
                operands = []
                while self.current_tok.type != TokenType.RPAREN:
                    operands.append(self.expr())
                return FunctionCallNodeWithOperands(token, operands)
        return IdentifierNode(token)

    def group_expr(self):
        self.advance()  # Consume '('
        expr = self.expr()
        self.advance()  # Consume ')'
        return expr

    def if_expr(self):
        self.advance()  # Consume 'if'
        condition = self.expr()
        if not isinstance(condition, ASTNode):
            condition = NumberNode(condition)  # Create a NumberNode for simple conditions
        
        true_branch = self.expr()
        if self.current_tok.type != TokenType.RPAREN:  # Check if there's a false branch
            false_branch = self.expr()
        else:
            false_branch = None  # No false branch provided
        
        return IfNode(condition, true_branch, false_branch)

    def cond_expr(self):
        self.advance()  # Consume 'cond'
        cases = []
        while self.current_tok.type != TokenType.RPAREN:
            condition = self.expr()
            expression = self.expr()
            cases.append((condition, expression))
        return CondNode(cases)

    
    def define_expr(self):
        self.advance()
        identifier = self.identifier_expr()

        value = self.expr()  # Parse the expression
        if isinstance(value, LambdaNode):
            user_defined_identifiers[identifier.token.value] = (
                IdentifierType.FUNCTION,
                value,
            )

        return DefineNode(identifier, value)

    def list_expr(self):
        self.advance() # Skip 'list'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        self.advance() # Skip ')'
        return ListNodes(elements)

    def let_expr(self):
        self.advance()  # Skip 'let'
        self.advance()  # Skip '('
        bindings = []
        while self.current_tok.type != TokenType.RPAREN:
            if self.current_tok.type == TokenType.LBRACKET:
                self.advance()  # Skip '['
                identifier = self.identifier_expr()
                value = self.expr()
                bindings.append((identifier, value))
                if self.current_tok.type == TokenType.RBRACKET:
                    self.advance()  # Skip ']'
            else:
                self.error("Expected '['")
        self.advance()  # Skip ')'
        expr = self.expr()
        # print(f"bindings: {bindings}")
        return LetNode(bindings, expr)

    def lambda_expr(self):
        self.advance()
        self.advance()
        params = []
        while self.current_tok.type != TokenType.RPAREN:
            identifier = self.identifier_expr()
            params.append(identifier)
        self.advance()
        expr = self.expr()
        return LambdaNode(params, expr)

    def number_expr(self):
        token = self.current_tok
        self.advance()
        return NumberNode(token.value)

import sys

def main(filename=None):
    lexer = Lexer()
    if filename:
        with open(filename, 'r') as file:
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
            #print ("tokens = " , tokens)
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

