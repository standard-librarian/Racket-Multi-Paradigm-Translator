from .ast_node import ASTNode


class ValuesNode(ASTNode):
    def __init__(self):
        pass

    def generate_python_code(self):
        return f"lambda i: i"
