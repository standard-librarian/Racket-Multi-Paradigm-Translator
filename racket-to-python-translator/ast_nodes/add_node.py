from .ast_node import ASTNode
from .number_node import NumberNode


class AddNode(ASTNode):
    def __init__(self, operands):
        self.operands = operands

    def generate_python_code(self):
        # add_all((2, 5, 7))
        output = "add_all(("
        for operand in self.operands:
            if isinstance(operand, NumberNode):
                output += f"{operand.value}, "
            else:
                output += operand.generate_python_code() + ", "

        output = output[:-2]
        output += "))"
        return output

    def __str__(self):
        return f"AddNode({self.operands})"

    def __repr__(self):
        return self.__str__()
