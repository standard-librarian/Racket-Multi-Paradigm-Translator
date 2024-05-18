from .ast_node import ASTNode


class StringNode(ASTNode):
    def __init__(self, token):
        self.token = token

    def generate_python_code(self):
        return repr(self.token.value)
