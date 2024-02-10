import ast
from ast import AST, FunctionDef, NodeTransformer

from .config import Config
from .helpers import generate_doc_string, make_docstring_node
from .model_parsers import parse_function_docstr


class FunctionTransformer(NodeTransformer):
    def __init__(self, config: Config, function_src: str) -> None:
        super().__init__()
        self._config: Config = config
        self._function_src = function_src

    def visit_FunctionDef(self, node: FunctionDef) -> None:
        ast_tree: AST = ast.parse(self._function_src)
        function_node: AST = ast_tree.body[0]
        docstring: str = ast.get_docstring(node=node)
        if function_node.name == node.name:
            if not docstring:
                src_code: str = ast.unparse(node)
                func_docstr: str = generate_doc_string(
                    src_code=src_code, config=self._config
                )
                doc_str: str = parse_function_docstr(func_docstr.strip())
                if doc_str:
                    dcstr_node: AST = make_docstring_node(doc_str)
                    node.body.insert(0, dcstr_node)
            elif self._config.overwrite_function_docstring:
                src_code: str = ast.unparse(node)
                func_docstr: str = generate_doc_string(
                    src_code=src_code, config=self._config
                )
                doc_str: str = parse_function_docstr(func_docstr.strip())
                if doc_str:
                    dcstr_node: AST = make_docstring_node(doc_str)
                    node.body[0] = dcstr_node
        return node
