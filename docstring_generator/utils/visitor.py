from __future__ import annotations

from abc import ABC, abstractmethod

from composite import File, Folder


class Visitor(ABC):
    def visit_File(self, file: File) -> None:
        print(f'visiting the file called "{file.name}"')

    def visit_Folder(self, folder: Folder) -> None:
        print(f'visiting the folder called "{folder.name}"')
