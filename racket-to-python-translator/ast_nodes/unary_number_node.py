from .ast_node import ASTNode
from .number_node import NumberNode


class UnaryNumberNode(ASTNode):
    def __init__(self, token, number: NumberNode):
        self.token = token
        self.number = number

    def generate_python_code(self):
        return f"{self.token.value}{self.number.generate_python_code()}"
