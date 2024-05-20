#!/usr/bin/python3
"""Print a square"""


def print_square(size):
    """print # squares"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for element in range(size):
            print("#", end="")
        print()
