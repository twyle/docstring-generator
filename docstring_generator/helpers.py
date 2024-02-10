import ast
import subprocess
from ast import AST, Constant, Expr, FunctionDef
from os import path

from .config import Config
from .llms import chatgpt
from .templates import function_prompt


def read_src(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def save_src(file_path: str, new_src: str) -> str:
    with open(file_path, 'w', encoding='utf-8') as f:
        return f.write(new_src)


def parse_src(file_src: str) -> AST:
    return ast.parse(file_src)


def print_src(src_tree: AST) -> None:
    print(ast.dump(src_tree, indent=4))


function_dcstr: str = '''
def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts two numbers

    Parameters
    ----------
    a : int or float
        The first number to subtract.
    b : int or float
        The second number to subtract.

    Returns
    -------
    int or float
        The result of subtracting b from a.
    """
    return a - b
'''


def generate_doc_string(src_code: str, config: Config) -> str:
    prompt_formatted_str: str = function_prompt.format(
        function_code=src_code, documentation_style=config.documentation_style
    )
    function_and_docstring: str = chatgpt.invoke(prompt_formatted_str)
    return function_and_docstring
    # return function_dcstr


def make_docstring_node(docstr: str):
    constant_str: Constant = Constant(docstr)
    return Expr(value=constant_str)


def format_file(file_path: str) -> None:
    """Format the file using black."""
    if path.exists(file_path):
        subprocess.run(['black', file_path], capture_output=True)
