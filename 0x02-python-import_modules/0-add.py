#!/usr/bin/python3

from add_0 import add as add1

a = 1
b = 2
result = add1(a, b)
print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    add1(a, b)
