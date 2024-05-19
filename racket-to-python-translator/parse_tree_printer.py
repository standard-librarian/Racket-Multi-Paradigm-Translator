from .ast_nodes.cond_node import CondNode
from .ast_nodes.function_call_with_operands_node import FunctionCallNodeWithOperands
from .ast_nodes.identifier_node import IdentifierNode
from .ast_nodes.if_node import IfNode
from .ast_nodes.lambda_node import LambdaNode
from .ast_nodes.number_node import NumberNode
from .ast_nodes.string_node import StringNode
from .ast_nodes.list_node import ListNodes
from .ast_nodes.comment_node import CommentNode
from .ast_nodes.ast_node import ASTNode


def print_parse_tree(node, indent="", last_child=True, label=None):
    tree_representation = ""

    branch_symbol = "└── " if last_child else "├── "

    if label is not None:  
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
        if isinstance(node, (str, int, float)):
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
    elif isinstance(node, CondNode):
        child_nodes = [(f"CASE {idx+1}", case) for idx, case in enumerate(node.cases)]
        for i, (case_label, case_contents) in enumerate(child_nodes):
            condition, result = case_contents
            if condition is None and result is None: 
                continue
            if condition is None and i == len(child_nodes) - 1:
                tree_representation += indent + "└── ELSE\n"
            else:
                tree_representation += indent + "├── " + case_label + "\n"
            new_indent = indent + ("│   " if last_child else "    ")
            if condition is not None:
                tree_representation += print_parse_tree(condition, new_indent, False, label="CONDITION")  
            if result is not None:
                tree_representation += print_parse_tree(result, new_indent, True, label="RESULT")  
        return tree_representation

    elif isinstance(node, NumberNode):
        child_nodes = [node.value]
    elif isinstance(node, CommentNode):
        child_nodes = [node.comment]
    elif isinstance(node, IdentifierNode):
        child_nodes = [node.token.value]
    elif isinstance(node, ListNodes):
        child_nodes = node.elements
    elif isinstance(node, LambdaNode):
        child_nodes = [
            ("EXPRESSION", node.expr),
            ("PARAMS", node.params),
        ]
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
            if isinstance(child_node, tuple):
                tree_representation += print_parse_tree(child_node, child_indent, i == len(child_nodes) - 1, label=label)
            elif isinstance(child_node, list):
                for j, sub_child in enumerate(child_node):
                    tree_representation += print_parse_tree(
                        sub_child, child_indent, j == len(child_node) - 1, label=label if j == 0 else None
                    )
            elif isinstance(child_node, ASTNode):
                tree_representation += print_parse_tree(
                    child_node, child_indent, i == len(child_nodes) - 1, label=label
                )
            else:
                tree_representation += f"{child_indent}└── {child}\n"
        else:
            tree_representation += print_parse_tree(
                child, child_indent, i == len(child_nodes) - 1
            )

    return tree_representation
