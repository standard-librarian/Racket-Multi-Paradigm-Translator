from ast_nodes.ast_node import ASTNode


class LambdaNode(ASTNode):
    def __init__(self, params, expr):
        self.params = params
        self.expr = expr

    def generate_python_code(self):
        params_str = ", ".join([param.generate_python_code() for param in self.params])
        return f"lambda {params_str}: {self.expr.generate_python_code()}"

    def __str__(self):
        return f"LambdaNode({self.params}, {self.expr})"

    def __repr__(self):
        return self.__str__()