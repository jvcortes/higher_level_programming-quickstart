#!/usr/bin/python3
"""
This module holds the definitions for task 8
"""
from numpy import array, matmul


def lazy_matrix_mul(m_a, m_b):
    """ Returns a matrix multiplication between two matrices.

    Args:
        m_a (list: int, float): first matrix
        m_b (list: int, float): second matrix
    """

    return matmul(array(m_a), array(m_b))
