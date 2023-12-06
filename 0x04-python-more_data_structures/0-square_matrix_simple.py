#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = len(matrix)
    rmatrix = matrix.copy()

    for i in range(n):
        rmatrix[i] = list(map(lambda x: x * x, matrix[i]))
    return rmatrix
