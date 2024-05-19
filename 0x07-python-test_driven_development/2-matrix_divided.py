#!/usr/bin/python3
"""Division in lists of lists"""


def matrix_divided(matrix, div):
    """Divide a matrix by an integer"""
    newMatrix = []
    for row in matrix:
        newrow = []
        for element in row:
            result = round(element / div, 2)
            newrow.append(result)
        newMatrix.append(newrow)
    return newMatrix
