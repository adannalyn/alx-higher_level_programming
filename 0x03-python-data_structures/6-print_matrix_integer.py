#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if len(num) < 3:
                print("{}".format(num), end=" ")
        print()


if __name__ == "__main__":
    pass
