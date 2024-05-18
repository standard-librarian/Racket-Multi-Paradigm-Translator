from .ast_node import ASTNode


class MaxNode(ASTNode):
    def __init__(self, args):
        self.args = args

    def generate_python_code(self):
        return f"max({', '.join([arg.generate_python_code() for arg in self.args])})"
