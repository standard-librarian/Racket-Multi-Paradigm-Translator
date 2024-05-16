from ast_nodes.ast_node import ASTNode

class ListNodes(ASTNode):
    def __init__(self, elements):
        self.elements = elements

    def generate_python_code(self):
        return f"list(({', '.join([element.generate_python_code() for element in self.elements])}))"
