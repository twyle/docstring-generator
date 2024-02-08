import ast
from _ast import FunctionDef
from ast import AST, Constant, Expr, NodeTransformer
from typing import Any

from utils import parse_src, read_src

function_dcstr: str = """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        First number to be added.
    b : int or float
        Second number to be added.

    Returns
    -------
    int or float
        Sum of a and b.
    """


def get_function_docstring() -> str:
    return function_dcstr


def make_docstring_node(docstr: str):
    constant_str: Constant = Constant(docstr)
    return Expr(value=constant_str)


class MyTransformer(NodeTransformer):
    def visit_FunctionDef(self, node: FunctionDef) -> FunctionDef:
        if node.name == 'add':
            add_dcstr: str = get_function_docstring()
            dcstr_node: AST = make_docstring_node(add_dcstr)
            node.body.insert(0, dcstr_node)
        return node


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    transformer: NodeTransformer = MyTransformer()
    new_tree = transformer.visit(src_tree)
    ast.fix_missing_locations(new_tree)
    new_module_code = ast.unparse(new_tree)
    print(new_module_code)


if __name__ == '__main__':
    main()
