from .ast_node import ASTNode


class StringNode(ASTNode):
    def __init__(self, token):
        self.token = token

    def generate_python_code(self):
        return repr(self.token.value)

    def __str__(self):
        return f"String({self.token.value})"

    def __repr__(self):
        return self.__str__()
