from .ast_node import ASTNode


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def generate_python_code(self):
        return str(self.value)
