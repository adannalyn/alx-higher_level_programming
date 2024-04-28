#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    num_list = []
    for row in matrix:
        temp = []
        for num in row:
            temp.append(num ** 2)
        num_list.append(temp)
    return num_list


if __name__ == "__main__":
    pass
