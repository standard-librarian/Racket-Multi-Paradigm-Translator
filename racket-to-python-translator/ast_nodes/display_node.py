from .ast_node import ASTNode


class DisplayNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr
        print(str(expr))

    def generate_python_code(self):
        return f"print({self.expr.generate_python_code()})"
