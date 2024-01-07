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

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
