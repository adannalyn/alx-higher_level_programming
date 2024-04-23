#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    for inte in my_list[::-1]:
        print("{:d}".format(inte))


if __name__ == "__main__":
    pass
