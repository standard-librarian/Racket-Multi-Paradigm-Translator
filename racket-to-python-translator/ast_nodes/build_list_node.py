from .ast_node import ASTNode


class BuildListNode(ASTNode):
    def __init__(self, size, generator):
        self.size = size
        self.generator = generator

    def generate_python_code(self):
        return f"list(map({self.generator.generate_python_code()}, range({self.size.generate_python_code()})))"

    def __str__(self):
        return f"BuildListNode({self.generator}({self.size}))"

    def __repr__(self):
        return self.__str__()
