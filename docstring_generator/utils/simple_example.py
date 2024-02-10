from dotenv import load_dotenv

load_dotenv()
import ast
import os
from ast import AST, FunctionDef, NodeVisitor

from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from utils import parse_src, read_src


def generate_doc_string(src_code: str) -> str:
    api_key: str = os.environ['OPENAI_API_KEY']

    llm: BaseLLM = OpenAI(temperature=0, api_key=api_key)

    function_prompt_template: str = """
    Generate python docstring for the given python function using the provided documentation style.
    Make sure to provide atleast two examples of the function usage only in the docstring as well
    as the exceptions that may be raised when using the function. Make sure to return the
    function and its docstring.
    Function code: {function_code}
    Documentation style: {documentation_style}
    """

    documentation_style: str = 'Numpy-Style'

    prompt = PromptTemplate.from_template(template=function_prompt_template)
    prompt_formatted_str: str = prompt.format(
        function_code=src_code, documentation_style=documentation_style
    )

    function_and_docstring: str = llm.invoke(prompt_formatted_str)
    return function_and_docstring


def parse_function_docstr(func_dcstr: str) -> str:
    src_tree: AST = parse_src(func_dcstr)
    func_node: FunctionDef = src_tree.body[0]
    doc_str: str = ast.get_docstring(func_node)
    return doc_str


class MyVisitor(NodeVisitor):
    def visit_FunctionDef(self, node: FunctionDef) -> None:
        if node.name == 'add':
            src_code: str = ast.unparse(node)
            func_docstr: str = generate_doc_string(src_code)
            doc_str: str = parse_function_docstr(func_docstr.strip())
            print(doc_str)


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    visitor = MyVisitor()
    visitor.visit(src_tree)


if __name__ == '__main__':
    main()
