import ast
from ast import AST, FunctionDef, NodeVisitor

from utils import parse_src, read_src


class MyVisitor(NodeVisitor):
    def visit_FunctionDef(self, node: FunctionDef) -> None:
        print(f'Getting the source code for the function: {node.name}')
        src_code: str = ast.unparse(node)
        print(src_code)


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    visitor = MyVisitor()
    visitor.visit(src_tree)


if __name__ == '__main__':
    main()
