from ast_nodes.ast_node import ASTNode

class SinNode(ASTNode):
    def __init__(self, elements):
        self.elements = elements

    def generate_python_code(self):
        number = self.elements[0].generate_python_code()  # number
        return f"math.sin({number})"

