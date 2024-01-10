#!/usr/bin/python3
"""Implements pascal triangle"""


def pascal_triangle(n):
    """
        returns thelist of lists
        Args:
            n (int): number of elements
        Returns: the list of lists
    """

    outer= []

    if n <= 0:
        return outer
    for i in range(n):
        inner = [1] * (i+1)
        outer.append(inner)
    for i in range(2, n):
        for j in range(1, i):
            outer[i][j] = outer[i - 1][j - 1] + outer[i - 1][j]
    return outer
