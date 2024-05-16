from ast_nodes.ast_node import ASTNode


class DefineNode(ASTNode):
    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr

    def generate_python_code(self):
        return f"{self.identifier.generate_python_code()} = {self.expr.generate_python_code()}"
