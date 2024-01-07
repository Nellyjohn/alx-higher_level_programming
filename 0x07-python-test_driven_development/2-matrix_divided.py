#!/usr/bin/python3
"""This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements.

    Args:
        matrix (int or float): First parameter.
        div (int or float): second prameter.

    Raises:
        TypeError: if matrix or div are not integers or float.
        ZeroDivisionError: if div is equal to 0.

    Returns:
        A new matrix.
    """

    for row in matrix[1:]:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")

    row_size = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
