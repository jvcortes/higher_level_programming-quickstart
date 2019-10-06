#!/usr/bin/python3
"""
This module holds the definitions for task 7
"""


def matrix_mul(m_a, m_b):
    """ Returns a matrix multiplication between two matrices.

    Args:
        m_a (list: int, float): first matrix
        m_b (list: int, float): second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if all(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if all(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    length = len(m_a[0])
    if not all(len(row) == length for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    length = len(m_b[0])
    if not all(len(row) == length for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    for row in m_a:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row_a in m_a:
        i = 0
        j = 0
        result_row = []
        result_row_item = 0
        while j < len(m_b[0]):
            while i < len(m_b):
                result_row_item += round(row_a[i] * m_b[i][j], 2)
                i += 1
            result_row.append(result_row_item)
            result_row_item = 0
            i = 0
            j += 1
        result.append(result_row)

    return result
