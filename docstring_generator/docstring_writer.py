import ast
from ast import AST, NodeTransformer
from queue import Empty, Queue

from .config import Config
from .helpers import format_file, parse_src, read_src, save_src
from .transformers import FunctionTransformer
from .walkers import FunctionVisitor


def process_file(source_code_queue: Queue, function_code_queue: Queue):
    while True:
        try:
            file_path: str = source_code_queue.get(timeout=1)
            print(f'processing the file: {file_path}')
            file_src: str = read_src(file_path=file_path)
            src_tree: AST = parse_src(file_src)
            visitor: FunctionVisitor = FunctionVisitor(
                function_code_queue=function_code_queue,
                file_path=file_path,
            )
            visitor.visit(src_tree)
            source_code_queue.task_done()
        except Empty:
            print('Terminating the file processing..')
            break


def process_function(config: Config, function_code_queue: Queue) -> None:
    while True:
        try:
            file_path, function_code = function_code_queue.get(timeout=1)
            # print(function_code)
            file_src: str = read_src(file_path=file_path)
            src_tree: AST = parse_src(file_src)
            # print_src(src_tree)
            transformer: NodeTransformer = FunctionTransformer(
                config=config, function_src=function_code
            )
            new_tree = transformer.visit(src_tree)
            ast.fix_missing_locations(new_tree)
            new_module_code = ast.unparse(new_tree)
            print(new_module_code)
            save_src(file_path=file_path, new_src=new_module_code)
            format_file(file_path=file_path)
            function_code_queue.task_done()
        except Empty:
            print('Terminating the function processing..')
            break
