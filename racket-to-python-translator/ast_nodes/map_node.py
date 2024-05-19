from .ast_node import ASTNode


class MapNode(ASTNode):
    def __init__(self, func, lst):
        self.func = func
        self.lst = lst

    def __repr__(self):
        return f"MapNode(func={self.func}, list={self.lst})"

    def generate_python_code(self):
        lst_code = self.lst.generate_python_code()
        return f"list(map({self.func.generate_python_code()}, {lst_code}))"
