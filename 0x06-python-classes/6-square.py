#!/usr/bin/python3
"""a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize size with zero"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get property of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set property of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get property of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set property of size"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    def area(self):
        """Returns: size(int): return the area"""
        return self.__size * self.__size

    def my_print(self):
        """print # in multiple times"""
        if self.__size == 0:
            print()
        for x in range(self.__position[1]):
            print("")
        for x in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
