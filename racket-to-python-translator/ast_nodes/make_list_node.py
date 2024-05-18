from .ast_node import ASTNode


class MakeListNode(ASTNode):
    def __init__(self, size, element):
        self.size = size
        self.element = element

    def generate_python_code(self):
        return f"[{self.element.generate_python_code()}] * {self.size.generate_python_code()}"

    def __str__(self):
        return f"MakeListNode({self.element}({self.size}))"

    def __repr__(self):
        return self.__str__()
