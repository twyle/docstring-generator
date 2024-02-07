from pydantic import BaseModel, Field


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
