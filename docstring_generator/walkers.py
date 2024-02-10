import ast
from ast import FunctionDef
from queue import Queue
from .helpers import read_src


class FunctionVisitor(ast.NodeVisitor):
    def __init__(
        self, function_code_queue: Queue, file_path: str
    ) -> None:
        super().__init__()
        self._function_code_queue = function_code_queue
        self._file_path = file_path

    def visit_FunctionDef(self, node: FunctionDef) -> None:
        function_code: str = ast.unparse(ast_obj=node)
        self._function_code_queue.put((self._file_path, function_code))
