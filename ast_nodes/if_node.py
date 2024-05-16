from ast_nodes.ast_node import ASTNode


class IfNode(ASTNode):
    def __init__(self, condition, true_branch, false_branch=None):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def generate_python_code(self):
        if self.false_branch:
            return f"({self.true_branch.generate_python_code()} if {self.condition.generate_python_code()} else {self.false_branch.generate_python_code()})"
        else:
            return f"({self.true_branch.generate_python_code()} if {self.condition.generate_python_code()} else None)"
