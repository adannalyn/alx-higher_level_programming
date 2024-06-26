#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


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
        self.__size = size

    @property
    def size(self):
        """get property of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """swet property of size"""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Returns:
            size(int): return the area
        """
        return self.__size * self.__size

    def my_print(self):
        """print # in multiple times"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
