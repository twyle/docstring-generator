import ast
from ast import AST, NodeVisitor
from typing import Any


def read_src(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def parse_src(file_src: str) -> AST:
    return ast.parse(file_src)


def print_src(src_tree: AST) -> None:
    print(ast.dump(src_tree, indent=4))


class GenericVisitor(NodeVisitor):
    def generic_visit(self, node: AST) -> Any:
        return super().generic_visit(node)
