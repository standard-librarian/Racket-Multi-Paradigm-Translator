from .ast_nodes.add_node import AddNode
from .ast_nodes.ast_node import ASTNode
from .ast_nodes.cond_node import CondNode
from .ast_nodes.define_node import DefineNode
from .ast_nodes.display_node import DisplayNode
from .ast_nodes.div_node import DivNode
from .ast_nodes.equal_node import EqualNode
from .ast_nodes.function_call_with_operands_node import FunctionCallNodeWithOperands
from .ast_nodes.greater_equal_node import GreaterEqualNode
from .ast_nodes.greater_node import GreaterNode
from .ast_nodes.identifier_node import IdentifierNode
from .ast_nodes.if_node import IfNode
from .ast_nodes.lambda_node import LambdaNode
from .ast_nodes.less_equal_node import LessEqualNode
from .ast_nodes.less_node import LessNode
from .ast_nodes.let_node import LetNode
from .ast_nodes.mul_node import MULTNode
from .ast_nodes.number_node import NumberNode
from .ast_nodes.string_node import StringNode
from .ast_nodes.sub_node import SubNode
from .ast_nodes.list_node import ListNodes
from .ast_nodes.sqrt_node import SqrtNode
from .ast_nodes.abs_node import AbsNode
from .ast_nodes.sin_node import SinNode
from .ast_nodes.cos_node import CosNode
from .ast_nodes.tan_node import TanNode
from .ast_nodes.round_node import RoundNode
from .ast_nodes.ceil_node import CeilNode
from .ast_nodes.floor_node import FloorNode


from .token_types import TokenType, IdentifierType

user_defined_identifiers = {}


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

        elif tok_type == TokenType.LESS:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                expr = self.expr()
                operands.append(expr)
            return LessNode(operands)

        elif tok_type == TokenType.GREATER:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                expr = self.expr()
                operands.append(expr)
            return GreaterNode(operands)

        elif tok_type == TokenType.LESS_EQUAL:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                expr = self.expr()
                operands.append(expr)
            return LessEqualNode(operands)

        elif tok_type == TokenType.GREATER_EQUAL:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                expr = self.expr()
                operands.append(expr)
            return GreaterEqualNode(operands)

        elif tok_type == TokenType.EQUAL:
            self.advance()
            operands = []
            while self.current_tok.type != TokenType.RPAREN:
                expr = self.expr()
                operands.append(expr)
            return EqualNode(operands)

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
        elif tok_type == TokenType.NUMBER:
            return self.number_expr()
        elif tok_type == TokenType.LIST:
            return self.list_expr()
        elif tok_type == TokenType.SQRT:
            return self.sqrt_expr()
        elif tok_type == TokenType.ABS:
            return self.abs_expr()
        elif tok_type == TokenType.SIN:
            return self.sin_expr()
        elif tok_type == TokenType.COS:
            return self.cos_expr()
        elif tok_type == TokenType.TAN:
            return self.tan_expr()
        elif tok_type == TokenType.ROUND:
            return self.round_expr()
        elif tok_type == TokenType.CEIL:
            return self.ceil_expr()
        elif tok_type == TokenType.FLOOR:
            return self.floor_expr()

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
            condition = NumberNode(
                condition
            )  # Create a NumberNode for simple conditions

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

    def list_expr(self):
        self.advance()  # Skip 'list'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return ListNodes(elements)

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

    def sqrt_expr(self):
        # ( sqrt expr )
        self.advance() # Skip 'sqrt'
        elements = []  # expr 
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        self.advance()
        return SqrtNode(elements)
    
    def abs_expr(self):
        # ( abs number )
        self.advance() # Skip 'abs'
        elements = []  # expr 
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return AbsNode(elements)
    
    def sin_expr(self):
        # ( sin number )
        self.advance() # Skip 'sin'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return SinNode(elements)
    
    def cos_expr(self):
        # ( cos number )
        self.advance() # Skip 'cos'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return CosNode(elements)
   
    def tan_expr(self):
        # ( tan number )
        self.advance() # Skip 'tan'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return TanNode(elements)

    def round_expr(self):
        # ( round number )
        self.advance() # Skip 'round'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return RoundNode(elements)

    def ceil_expr(self):
        # ( ceil number )
        self.advance() # Skip 'ceil'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return CeilNode(elements)
    
    def floor_expr(self):
        # ( floor number )
        self.advance() # Skip 'floor'
        elements = []
        while self.current_tok.type != TokenType.RPAREN:
            elements.append(self.expr())
        return FloorNode(elements)


    def number_expr(self):
        token = self.current_tok
        self.advance()
        return NumberNode(token.value)
