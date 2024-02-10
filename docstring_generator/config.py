from typing import Optional

from pydantic import BaseModel, Field


class Config(BaseModel):
    root_directory: list[str] = Field(
        description='The path to the source code directory'
    )
    directories_ignore: set[str] = Field(
        description='Directories to ignore',
        default=set(['venv', '.venv', '__pycache__', '.git', 'build', 'dist', 'docs']),
    )
    files_ignore: set[str] = Field(
        description='Files to ignore',
        default_factory=set,
    )
    overwrite_function_docstring: Optional[bool] = Field(
        description='Whether or not to overwrite the existing function docstring',
        default=False,
    )
    documentation_style: Optional[str] = Field(
        description='The format of documentation to use',
        default='Numpy-Style',
        enum=['Numpy-Style', 'Google-Style', 'Sphinx-Style'],
    )
