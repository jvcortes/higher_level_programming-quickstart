#!/usr/bin/python3
"""

This module contains the function definition for task 1.

"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix (list: int, float): provided matrix, all of its rows must
            have the same size.
        div (int, float): divisor.
    """

    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix:

        if isinstance(matrix[0], list):
            length = len(matrix[0])
            if not all(len(x) == length for x in matrix):
                raise TypeError("Each row of the matrix must have the "
                                "same size")
        else:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        for row in matrix:
            if all(isinstance(item, (int, float)) for item in row):
                result.append([round(i / div, 2) for i in row])
            else:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    return result
