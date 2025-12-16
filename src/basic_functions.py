def add(a:str, b):
    """
    Return the sum of two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of `a` and `b`.
    """
    return a + b 


def subtract(a: float, b: float) -> float:
    """
    Return the difference between two numbers.

    Parameters
    ----------
    a : float
        The number to subtract from.
    b : float
        The number to subtract.

    Returns
    -------
    float
        The difference of `a` and `b`.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The product of `a` and `b`.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the division of one number by another.

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Returns
    -------
    float
        The quotient of `a` divided by `b`.

    Raises
    ------
    ZeroDivisionError
        If `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
