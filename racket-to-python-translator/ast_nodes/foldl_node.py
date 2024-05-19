from .ast_node import ASTNode


class FoldlNode(ASTNode):
    def __init__(self, func, init_val, lst):
        self.func = func
        self.init_val = init_val
        self.lst = lst

    def __repr__(self):
        return f"FoldlNode(func={self.func}, init_val={self.init_val}, lst={self.lst})"

    def generate_python_code(self):
        return f"functools.reduce({self.func.generate_python_code()}, {self.lst.generate_python_code()}, {self.init_val.generate_python_code()})"
