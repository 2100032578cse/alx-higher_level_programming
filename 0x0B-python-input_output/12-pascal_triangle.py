#!/usr/bin/python3
"""Implements pascal triangle"""


def pascal_triangle(n):
    """
        returns thelist of lists
        Args:
            n (int): number of elements
        Returns: the list of lists
    """

    row = [0]
    p = [1]
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        triangle.append(row)
        row = (lc+rw for lc, rw i n zip(row + t, t + row))
    return triangle
