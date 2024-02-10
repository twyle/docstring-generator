import operator


def add(a: int | float, b: int | float) -> int | float:
    """Returns the sum of two numbers.

    Parameters
    ----------
    a : int or float
        First number to be added.
    b : int or float
        Second number to be added.

    Returns
    -------
    int or float
        Sum of a and b.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(2.5, 3.5)
    6.0

    Raises
    ------
    TypeError
        If either a or b is not an int or float."""
    return operator.add(a, b)


def subtract(a: int | float, b: int | float) -> int | float:
    """Returns the difference between two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The difference between a and b.

    Examples
    --------
    >>> subtract(5, 3)
    2
    >>> subtract(3.5, 2.5)
    1.0

    Raises
    ------
    TypeError
        If either a or b is not an int or float."""
    return operator.sub(a, b)


def divide(a: int | float, b: int | float) -> float:
    """Returns the quotient of two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    float
        The quotient of a divided by b.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    >>> divide(3.5, 0.5)
    7.0

    Raises
    ------
    TypeError
        If either a or b is not an int or float.
    ZeroDivisionError
        If b is 0."""
    return operator.truediv(a, b)


def mutiply(a: int | float, b: int | float) -> int | float:
    """Returns the product of two numbers.

    Parameters
    ----------
    a : int or float
        First number to be multiplied.
    b : int or float
        Second number to be multiplied.

    Returns
    -------
    int or float
        Product of a and b.

    Examples
    --------
    >>> multiply(2, 3)
    6
    >>> multiply(2.5, 4)
    10.0

    Raises
    ------
    TypeError
        If either a or b is not an int or float."""
    return operator.mul(a, b)
