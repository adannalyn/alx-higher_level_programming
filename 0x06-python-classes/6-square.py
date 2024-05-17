#!/usr/bin/python3
"""a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize size with zero"""
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position  = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
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
