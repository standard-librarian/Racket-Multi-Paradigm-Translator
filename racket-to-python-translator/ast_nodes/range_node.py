from .ast_node import ASTNode


class RangeNode(ASTNode):
    def __init__(self, start, end=None, step=None):
        self.start = start.generate_python_code()
        self.end = end.generate_python_code() if end is not None else None
        self.step = step.generate_python_code() if step is not None else None

    def generate_python_code(self):
        if self.end is None:
            return f"range({self.start})"
        elif self.step is None:
            return f"range({self.start}, {self.end})"
        else:
            return f"range({self.start}, {self.end}, {self.step})"

    def __str__(self):
        return f"RangeNode(start={self.start}, end={self.end}, step={self.step})"

    def __repr__(self):
        return self.__str__()
