#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix, "-->$")

try:
    matrix = [[3, 9], [12, 15, 3]]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)
try:
    matrix = [[3, "9"], [12, 3]]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)

try:
    matrix = [[3, 9], [12, 3]]
    print(matrix_divided(matrix, "2"))
    print(matrix)
except Exception as e:
    print(e)

matrix = [
    [3]
]
print(matrix_divided(matrix, 3))
print(matrix)
