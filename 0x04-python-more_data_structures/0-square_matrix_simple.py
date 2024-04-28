#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    num_list = []
    for row in matrix:
        for num in row:
            num_list.append(num * 2)
    return num_list


if __name__ == "__main__":
    pass
