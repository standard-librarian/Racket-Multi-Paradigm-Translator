from .ast_node import ASTNode


class MinNode(ASTNode):
    def __init__(self, args):
        self.args = args

    def generate_python_code(self):
        return f"min({', '.join([arg.generate_python_code() for arg in self.args])})"
