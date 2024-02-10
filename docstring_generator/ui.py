import os
from argparse import ArgumentParser, Namespace
from os import path

from .config import Config


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        prog='docstring-generator',
        description='Generate docstrings for your python projects',
        epilog='Thanks for using %(prog)s! :)',
    )
    parser.add_argument('--path', nargs='*', default=['.'], type=str)
    parser.add_argument('--config-file', nargs='?', default='', type=str)
    parser.add_argument('--OPENAI_API_KEY', nargs='?', default='', type=str)
    parser.add_argument(
        '--overwrite-function-docstring', nargs='?', default=False, type=bool
    )
    parser.add_argument('--directories-ignore', nargs='*', default=[], type=str)
    parser.add_argument('--files-ignore', nargs='*', default=[], type=str)
    parser.add_argument(
        '--documentation-style',
        nargs='?',
        default='Numpy-Style',
        choices=['Numpy-Style', 'Google-Style', 'Sphinx-Style'],
        type=str,
    )
    args = parser.parse_args()
    paths: list[str] = args.path
    for entry in paths:
        if not path.exists(entry):
            print(f"The target path '{entry}' doesn't exist")
            raise SystemExit(1)
    if args.OPENAI_API_KEY:
        os.environ['OPENAI_API_KEY'] = args.OPENAI_API_KEY
    if not os.environ.get('OPENAI_API_KEY', None):
        print('You have not provided the open ai api key.')
        raise SystemExit(1)
    return args


def create_application_config(args: Namespace) -> Config:
    config: Config = Config(
        root_directory=set(args.path),
        overwrite_function_docstring=args.overwrite_function_docstring,
        documentation_style=args.documentation_style,
    )
    config.directories_ignore.update(set(args.directories_ignore))
    config.files_ignore.update(set(args.files_ignore))
    return config
