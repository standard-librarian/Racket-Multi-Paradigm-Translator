from ast_nodes.ast_node import ASTNode


class LetNode(ASTNode):
    def __init__(self, bindings, expr):
        self.bindings = bindings
        self.expr = expr

    def generate_python_code(self):
        bindings_str = ", ".join(
            [
                f"{identifier.generate_python_code()} = {value.generate_python_code()}"
                for identifier, value in self.bindings
            ]
        )
        "(lambda x=3, y=x+1: print(x, y)) ()"

        return f"(lambda {bindings_str}: {self.expr.generate_python_code()})()"

    def __str__(self):
        return f"LetDefinitionNode({self.identifier}, {self.expr})"

    def __repr__(self):
        return self.__str__()


class LetDefinitionNode(ASTNode):
    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr

    def generate_python_code(self):
        return f"{self.identifier.generate_python_code()} = {self.expr.generate_python_code()}"

    def __str__(self):
        return f"LetDefinitionNode({self.identifier}, {self.expr})"

    def __repr__(self):
        return self.__str__()
