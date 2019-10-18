#!/usr/bin/python3
"""
This module contains the function definition for task 14.
"""


def pascal_triangle(n):
    """ Returns a list containing a n sized Pascal's triangle.

    Args:
        n (int): size of the triangle
    """
    triangle = []
    if n > 0:
        for i in range(0, n):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1, 1])
            else:
                triangle.append([])
                for j in range(0, i + 1):
                    if j in (0, i):
                        triangle[i].append(1)
                    else:
                        triangle[i].append(
                            triangle[i - 1][j - 1] +
                            triangle[i - 1][j])
    return triangle
