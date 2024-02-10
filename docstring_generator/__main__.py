from argparse import Namespace

from .config import Config
from .docstring_generator import generate_project_docstrings
from .extensions import function_code_queue, source_code_queue
from .ui import create_application_config, parse_arguments


def main():
    args: Namespace = parse_arguments()
    config: Config = create_application_config(args)
    generate_project_docstrings(
        config=config,
        source_code_queue=source_code_queue,
        function_code_queue=function_code_queue,
    )


if __name__ == '__main__':
    main()
