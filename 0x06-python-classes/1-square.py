#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """A class representing a square"""

    def __init__(self, size):
        """
        Initialize size with a given size

        Parameters:
            size: the size
        """
        self.__size = size

    def get_size(self):
        """
        Accessing a private instance

        Return:
            size: the variable
        """
        return self.__size
square = Square(6)
