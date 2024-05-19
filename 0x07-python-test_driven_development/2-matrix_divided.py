#!/usr/bin/python3
"""Division in lists of lists"""


def matrix_divided(matrix, div):
    """Divide a matrix by an integer"""
    newMatrix = []
    for row in matrix:
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
        newrow = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            result = round(element / div, 2)
            newrow.append(result)
        newMatrix.append(newrow)
    return newMatrix
