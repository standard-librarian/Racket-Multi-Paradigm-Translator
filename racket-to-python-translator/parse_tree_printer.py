from .ast_nodes.add_node import AddNode
from .ast_nodes.cond_node import CondNode
from .ast_nodes.define_node import DefineNode
from .ast_nodes.display_node import DisplayNode
from .ast_nodes.div_node import DivNode
from .ast_nodes.equal_node import EqualNode
from .ast_nodes.function_call_with_operands_node import FunctionCallNodeWithOperands
from .ast_nodes.greater_equal_node import GreaterEqualNode
from .ast_nodes.greater_node import GreaterNode
from .ast_nodes.identifier_node import IdentifierNode
from .ast_nodes.if_node import IfNode
from .ast_nodes.lambda_node import LambdaNode
from .ast_nodes.less_equal_node import LessEqualNode
from .ast_nodes.less_node import LessNode
from .ast_nodes.let_node import LetNode
from .ast_nodes.mul_node import MULTNode
from .ast_nodes.number_node import NumberNode
from .ast_nodes.string_node import StringNode
from .ast_nodes.sub_node import SubNode
from .ast_nodes.comment_node import CommentNode
from .ast_nodes.ast_node import ASTNode


def print_parse_tree(node, indent="", last_child=True, label=None):
    tree_representation = ""

    branch_symbol = "└── " if last_child else "├── "

    if label is not None:  # Check if a label is provided and not empty
        node_info = f"{branch_symbol}{label}"
        tree_representation += indent + node_info + "\n"
        child_indent = indent + ("    " if last_child else "│   ")
        indent = child_indent
        node_info = f"{branch_symbol}{type(node).__name__}"
        tree_representation += indent + node_info + "\n"
    elif indent == "":
        tree_representation += type(node).__name__ + "\n"
        node_info = ""
    else:
        if isinstance(node, (str, int)):
            node_info = f"{branch_symbol}{node}"
        else:
            node_info = f"{branch_symbol}{type(node).__name__}"
    if node_info and label is None:
        tree_representation += indent + node_info + "\n"

    child_indent = indent + ("    " if last_child else "│   ")
    child_nodes = []

    if hasattr(node, "operands"):
        child_nodes = node.operands
    elif isinstance(node, IfNode):
        child_nodes = [
            ("ELSE", node.false_branch),
            ("THEN", node.true_branch),
            ("CONDITION", node.condition),
        ]
    elif isinstance(node, NumberNode):
        child_nodes = [node.value]
    elif isinstance(node, IdentifierNode):
        child_nodes = [node.token.value]
    elif isinstance(node, StringNode):
        child_nodes = [f"'{node.token.value}'"]
    else:
        child_nodes = [
            getattr(node, attr_name)
            for attr_name in dir(node)
            if isinstance(getattr(node, attr_name, None), ASTNode)
        ]
    child_nodes.reverse()
    for i, child in enumerate(child_nodes):
        if isinstance(child, tuple):
            label, child_node = child
            tree_representation += print_parse_tree(
                child_node, child_indent, i == len(child_nodes) - 1, label=label
            )
        else:
            tree_representation += print_parse_tree(
                child, child_indent, i == len(child_nodes) - 1
            )

    return tree_representation
