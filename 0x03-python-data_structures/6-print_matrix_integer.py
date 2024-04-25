#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first = True
        for num in row:
            if not first:
                print(" ", end="")
            print("{}".format(num), end="")
            first = False
        print()


if __name__ == "__main__":
    pass
