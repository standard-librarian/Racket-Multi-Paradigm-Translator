from ast_nodes.ast_node import ASTNode


class EqualNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def generate_python_code(self):
        return f"({self.left.generate_python_code()} == {self.right.generate_python_code()})"
