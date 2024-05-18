#!/usr/bin/python3
"""
Addition of two integers

Functions: add_integer(a, b=0)
"""


def add_integer(a, b=98):
    """Add two integers
    param a: first integer
    param b: second integer"""
    result = 0
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
