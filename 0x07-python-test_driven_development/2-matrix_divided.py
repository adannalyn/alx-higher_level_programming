#!/usr/bin/python3
"""Division in lists of lists"""


def matrix_divided(matrix, div):
    """Divide a matrix by an integer"""
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("matrix must have each row with the same size")
    newMatrix = []
    for row in matrix[0:]:
        newrow = []
        for element in row:
            result = round(element / div, 2)
            newrow.append(result)
        newMatrix.append(newrow)
    return newMatrix
