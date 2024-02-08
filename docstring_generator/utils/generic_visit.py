import ast
from ast import AST

from utils import parse_src, read_src


class MyVisitor(ast.NodeVisitor):
    def generic_visit(self, node: AST) -> None:
        print(f'entering {node.__class__.__name__}')
        super().generic_visit(node)


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    visitor = MyVisitor()
    visitor.visit(src_tree)


if __name__ == '__main__':
    main()
