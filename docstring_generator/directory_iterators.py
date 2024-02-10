from collections import deque
from collections.abc import Iterator
from os import listdir, path
from queue import Queue

from .config import Config
from .helpers import read_src


class DirectoryIterator(Iterator):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self._folders_ignore = set(config.directories_ignore)
        self._files_ignore = set(config.files_ignore)
        self._queue = deque(config.root_directory)  # adding the individual chars

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


def get_all_modules(config: Config, source_code_queue: Queue) -> None:
    """Iterate throug all the directories from the root directory."""
    for entry in config.root_directory:
        if path.isfile(entry):
            source_code_queue.put(entry)
        else:
            directory_iterator: DirectoryIterator = DirectoryIterator(config=config)
            for modules in directory_iterator:
                for module in modules:
                    source_code_queue.put(module)
