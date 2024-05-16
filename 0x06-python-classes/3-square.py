#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """
        Initialize size with zero

        Parameters:
            size(int): 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size * size

    def area(self):
        """
        Return:
            size(int): return the area
        """
        return self.__size
