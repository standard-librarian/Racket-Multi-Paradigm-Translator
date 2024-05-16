from ast_nodes.ast_node import ASTNode


class IdentifierNode(ASTNode):
    def __init__(self, token):
        self.token = token

    def generate_python_code(self):
        return self.token.value

    def __str__(self):
        return self.token.value

    def __repr__(self):
        return self.__str__()
