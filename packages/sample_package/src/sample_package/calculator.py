"""Mathematical utilities and a simple calculator implementation.

This module provides basic arithmetic helper functions as well as a
``Calculator`` class that supports configurable rounding precision.
The functions are designed to be simple, reusable, and easy to test.
"""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of ``a`` and ``b``.
    """
    return a + b


def divide(a: float, b: float) -> float:
    """Divide one number by another.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of dividing ``a`` by ``b``.

    Raises:
        ValueError: If ``b`` is equal to zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """A simple calculator supporting configurable precision.

    Attributes:
        precision (int): Number of decimal places used for rounding results.
    """

    def __init__(self, precision: int = 2):
        """Initialize the calculator.

        Args:
            precision (int, optional): Number of decimal places for rounding.
                Defaults to 2.
        """
        self.precision = precision

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and round the result.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The rounded product of ``a`` and ``b``.
        """
        return round(a * b, self.precision)

    def power(self, base: float, exponent: float) -> float:
        """Raise a number to a given power and round the result.

        Args:
            base (float): The base value.
            exponent (float): The exponent value.

        Returns:
            float: The rounded result of ``base`` raised to ``exponent``.
        """
        return round(base**exponent, self.precision)
