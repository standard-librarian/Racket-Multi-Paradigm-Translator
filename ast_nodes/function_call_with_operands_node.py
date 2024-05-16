from ast_nodes.ast_node import ASTNode


class FunctionCallNodeWithOperands(ASTNode):
    def __init__(self, token, operands):
        self.token = token
        self.operands = operands

    def generate_python_code(self):
        output = f"{self.token.value}("
        for operand in self.operands:
            output += f"{operand.generate_python_code()}, "
        output = output[:-2]
        output += ")"
        return output

    def __str__(self):
        return self.token.value

    def __repr__(self):
        return self.__str__()
