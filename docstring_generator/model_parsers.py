from __future__ import annotations

import ast
from abc import ABC, abstractmethod
from ast import AST, FunctionDef

from .helpers import parse_src


class Parser(ABC):
    @abstractmethod
    def set_next(self, parser: Parser) -> Parser:
        pass

    @abstractmethod
    def parse(self, docstring: str) -> str:
        pass


class AbstractParser(Parser):
    _next_parser: Parser = None

    def set_next(self, parser: Parser) -> Parser:
        self._next_parser = parser
        return parser

    @abstractmethod
    def parse(self, docstring: str) -> str:
        if self._next_parser:
            return self._next_parser.parse(docstring)
        print('Unable to parse the docstring generated.')
        print('################################')
        print(docstring)
        print('################################')
        return None


class DefaultParser(AbstractParser):
    def parse(self, docstring: str) -> str:
        try:
            src_tree: AST = parse_src(docstring)
            func_node: FunctionDef = src_tree.body[0]
            doc_str: str = ast.get_docstring(func_node)
        except Exception:
            return super().parse(docstring)
        else:
            return doc_str


model_parser: Parser = DefaultParser()


def parse_function_docstr(func_dcstr: str) -> str:
    return model_parser.parse(docstring=func_dcstr)
