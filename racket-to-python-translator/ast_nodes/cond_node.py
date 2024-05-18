from .ast_node import ASTNode


class CondNode(ASTNode):
    def __init__(self, cases):
        self.cases = cases

    def generate_python_code(self):
        return f"({next((expr.generate_python_code() for cond, expr in self.cases if cond), None)})"
