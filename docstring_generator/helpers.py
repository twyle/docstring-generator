from collections import deque
from collections.abc import Iterator
from os import listdir, path

from .config import Config


class DirectoryIterator(Iterator):
    def __init__(self, config: Config) -> None:
        super().__init__()
        if not path.exists(config.root_directory):
            raise ValueError(
                f'No such directory or file "{config.root_directory}" exists.'
            )
        if path.isfile(config.root_directory):
            raise ValueError('The root directory should be a file.')
        self._folders_ignore = set(config.folders_ignore)
        self._files_ignore = set(config.files_ignore)
        self._queue = deque(config.root_directory)

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
