#!/usr/bin/python3
for number in range(9):
    for numbers in range(number + 1, 10):
        if numbers != 9 or number != 8:
            print("{}{}".format(number, numbers), end=", ")
        else:
            print("{}{}".format(number, numbers))
