from .ast_node import ASTNode


class CondNode(ASTNode):
    def __init__(self, cases):
        self.cases = cases

    def generate_python_code(self):
        return self.generate_python_code_helper(self.cases)

    def generate_python_code_helper(self, cases):
        if len(cases) == 0:
            return "pass"
        else:
            for idx in range(len(cases)):
                condition, expression = cases[idx]
                if condition is None and expression is None:
                    continue
                if idx == 0:
                    output = f"if {condition.generate_python_code()}:\n"
                    output += f"    return {expression.generate_python_code()}"
                elif idx < len(cases) - 1 and condition is not None:
                    output += f"\nelif {condition.generate_python_code()}:\n"
                    output += f"    return {expression.generate_python_code()}"
                elif idx == len(cases) - 1:
                    output += f"\nelse:\n"
                    output += f"    return {expression.generate_python_code()}"
                else:
                    output += f"\nelse:\n"
                    output += f"    return {expression.generate_python_code()}"

            return output

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "CondNode"
