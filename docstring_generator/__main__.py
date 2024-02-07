from .config import Config
from .helpers import DirectoryIterator


def main():
    root_dir: str = '.'
    folders_ignore: list[str] = ['venv', '__pycache__', '.git', '.venv']
    config: Config = Config(
        root_directory=root_dir,
    )
    config.folders_ignore.extend(folders_ignore)
    directory_iterator: DirectoryIterator = DirectoryIterator(config=config)
    for files in directory_iterator:
        print(files)


if __name__ == '__main__':
    main()
