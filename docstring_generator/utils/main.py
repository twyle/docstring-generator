from ast import AST

from utils import parse_src, print_src, read_src


def main():
    file_path: str = './docstring_generator/utils/functions.py'
    src: str = read_src(file_path=file_path)
    src_tree: AST = parse_src(src)
    print_src(src_tree)


if __name__ == '__main__':
    main()
