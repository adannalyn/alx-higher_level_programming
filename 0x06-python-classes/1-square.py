#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    def __init__(self, size):
        self.__size = size
    def get_size(self):
        return self.__size
square = Square(6)
print(square.get_size())
