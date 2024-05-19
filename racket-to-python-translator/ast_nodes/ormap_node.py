from .ast_node import ASTNode


class OrmapNode(ASTNode):
    def __init__(self, func, lst):
        self.func = func
        self.lst = lst

    def __repr__(self):
        return f"OrmapNode(func={self.func}, lst={self.lst})"

    def generate_python_code(self):
        return f"any(map({self.func.generate_python_code()}, {self.lst.generate_python_code()}))"