from .ast_node import ASTNode


class FilterNode(ASTNode):
    def __init__(self, predicate, lst):
        self.predicate = predicate
        self.lst = lst

    def __repr__(self):
        return f"FilterNode(predicate={self.predicate}, lst={self.lst})"

    def generate_python_code(self):
        return f"list(filter({self.predicate.generate_python_code()}, {self.lst.generate_python_code()}))"
