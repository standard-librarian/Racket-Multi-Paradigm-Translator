from .ast_node import ASTNode


class CommentNode(ASTNode):
    def __init__(self, comment: str):
        self.comment = comment

    def generate_python_code(self):
        output = "#"
        if self.comment.startswith(";"):
            self.comment = self.comment[1:]
        output += self.comment
        return output
