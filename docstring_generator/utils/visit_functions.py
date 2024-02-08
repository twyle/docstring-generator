import ast
from _ast import FunctionDef
from ast import AST
from typing import Any

from utils import parse_src, read_src


class MyVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        print(f'entering {node.name}')


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    visitor = MyVisitor()
    visitor.visit(src_tree)


if __name__ == '__main__':
    main()
