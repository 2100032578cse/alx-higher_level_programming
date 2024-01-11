#!/usr/bin/python3
"""
for "2-matrix_divided"  modeule
and all funcs related
"""


def matrix_divided(matrix, div):
    """ all elements of matrix will be devided by div"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    size = None
    for lst in matrix:
        if type(lst) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(lst)
        elif size != len(lst):
            raise TypeError("Each row of the matrix must have the same size")
        for i in lst:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in lst] for lst in matrix]
