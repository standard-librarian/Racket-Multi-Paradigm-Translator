from .ast_node import ASTNode
from .number_node import NumberNode


class GreaterNode(ASTNode):
    def __init__(self, operands):
        self.operands = operands

    def generate_python_code(self):
        output = "all_gt(("
        for operand in self.operands:
            if isinstance(operand, NumberNode):
                output += f"{operand.value}, "
            else:
                output += operand.generate_python_code() + ", "
        output = output[:-2]
        output += "))"
        return output

    def __str__(self):
        return f"GreateNode({self.operands})"

    def __repr__(self):
        return self.__str__()