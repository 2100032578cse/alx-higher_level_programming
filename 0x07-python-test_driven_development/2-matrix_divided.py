#!/usr/bin/python3
"""
for "2-matrix_divided"  modeule
and all funcs related
"""


def matrix_divided(matrix, div):
    """ all elements of matrix will be devided by div"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None

