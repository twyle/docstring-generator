from ast import AST

from utils import parse_src, print_src

src: str = '''
def add(a, b):
    """
    Adds two numbers together.

    Parameters
    ----------
    a : int or float
        First number to be added.
    b : int or float
        Second number to be added.

    Returns
    -------
    int or float
        Sum of the two numbers.

    Raises
    ------
    TypeError
        If either a or b is not an int or float.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(2.5, 3.5)
    6.0
    >>> add("2", 3)
    TypeError: a must be an int or float
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be an int or float")

    return a + b
'''


def main():
    src_tree: AST = parse_src(src)
    print_src(src_tree)


if __name__ == '__main__':
    main()
