import ast
from _ast import FunctionDef
from ast import AST
from typing import Any

from utils import parse_src, read_src


class MyVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        print(f'entering {node.name}')
        docstring: str = ast.get_docstring(node=node)
        if docstring:
            print(f'The function "{node.name}" has docstring.')
            print(docstring)
        else:
            print(f'The function "{node.name}" has no docstring.')


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    visitor = MyVisitor()
    visitor.visit(src_tree)


if __name__ == '__main__':
    main()
