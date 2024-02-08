import operator


def add(a: int | float, b: int | float) -> int | float:
    return operator.add(a, b)


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts two numbers

    Parameters
    ----------
    a : int or float
        The first number to subtract.
    b : int or float
        The second number to subtract.

    Returns
    -------
    int or float
        The result of subtracting b from a.
    """
    return a - b
