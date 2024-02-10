from dotenv import load_dotenv

load_dotenv()
import ast
import os
from ast import AST, Constant, Expr, FunctionDef, NodeTransformer
from collections import deque
from collections.abc import Iterator
from os import listdir, path

from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from pydantic import BaseModel, Field
from utils import parse_src, print_src, read_src


class Config(BaseModel):
    root_directory: str = Field(description='The path to the source code directory')
    folders_ignore: list[str] = Field(
        description='Directories to ignore',
        default=['venv', '.venv', '__pycache__', '.git', 'build', 'dist', 'docs'],
    )
    files_ignore: list[str] = Field(
        description='Files to ignore',
        default_factory=list,
    )


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


def generate_doc_string(src_code: str) -> str:
    # api_key: str = os.environ['OPENAI_API_KEY']

    # llm: BaseLLM = OpenAI(temperature=0, api_key=api_key)

    # function_prompt_template: str = """
    # Generate python docstring for the given python function using the provided documentation style.
    # Make sure to provide atleast two examples of the function usage only in the docstring as well
    # as the exceptions that may be raised when using the function. Make sure to return the
    # function and its docstring.
    # Function code: {function_code}
    # Documentation style: {documentation_style}
    # """

    # documentation_style: str = 'Numpy-Style'

    # prompt = PromptTemplate.from_template(template=function_prompt_template)
    # prompt_formatted_str: str = prompt.format(
    #     function_code=src_code, documentation_style=documentation_style
    # )

    # function_and_docstring: str = llm.invoke(prompt_formatted_str)
    # return function_and_docstring
    return function_dcstr


def parse_function_docstr(func_dcstr: str) -> str:
    src_tree: AST = parse_src(func_dcstr)
    func_node: FunctionDef = src_tree.body[0]
    doc_str: str = ast.get_docstring(func_node)
    return doc_str


def make_docstring_node(docstr: str):
    constant_str: Constant = Constant(docstr)
    return Expr(value=constant_str)


class MyTransformer(NodeTransformer):
    def visit_FunctionDef(self, node: FunctionDef) -> None:
        src_code: str = ast.unparse(node)
        func_docstr: str = generate_doc_string(src_code)
        doc_str: str = parse_function_docstr(func_docstr.strip())
        dcstr_node: AST = make_docstring_node(doc_str)
        node.body.insert(0, dcstr_node)
        return node


def process_file(file_path: str) -> str:
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    # print_src(src_tree)
    transformer: NodeTransformer = MyTransformer()
    new_tree = transformer.visit(src_tree)
    ast.fix_missing_locations(new_tree)
    new_module_code = ast.unparse(new_tree)
    print(new_module_code)


class DirectoryIterator(Iterator):
    def __init__(self, config: Config) -> None:
        super().__init__()
        if not path.exists(config.root_directory):
            raise ValueError(
                f'No such directory or file "{config.root_directory}" exists.'
            )
        if path.isfile(config.root_directory):
            raise ValueError('The root directory should be a folder.')
        self._folders_ignore = set(config.folders_ignore)
        self._files_ignore = set(config.files_ignore)
        self._queue = deque([config.root_directory])  # adding the individual chars

    def __iter__(self) -> Iterator:
        return super().__iter__()

    def __next__(self) -> list[str]:
        if self._queue:
            files: list[str] = list()
            for _ in range(len(self._queue)):
                directory: str = self._queue.popleft()
                for entry in listdir(directory):
                    entry_path: str = path.join(directory, entry)
                    if (
                        path.isfile(entry_path)
                        and self._is_python_file(entry_path)
                        and entry not in self._files_ignore
                    ):
                        files.append(entry_path)
                    elif path.isdir(entry_path) and entry not in self._folders_ignore:
                        self._queue.append(entry_path)
            return files
        else:
            raise StopIteration()

    def _is_python_file(self, file_path: str) -> bool:
        return file_path.split('.')[-1] == 'py'


def main():
    # root_dir: str = './docstring_generator/utils/data'
    root_dir: str = './docstring_generator/'
    folders_ignore: list[str] = ['venv', '__pycache__', '.git', '.venv']
    config: Config = Config(
        root_directory=root_dir,
    )
    config.folders_ignore.extend(folders_ignore)
    directory_iterator: DirectoryIterator = DirectoryIterator(config=config)
    for files in directory_iterator:
        for file in files:
            process_file(file_path=file)


if __name__ == '__main__':
    main()
