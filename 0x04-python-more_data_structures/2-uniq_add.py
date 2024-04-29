#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    set_list = set(my_list)
    new_list = list(set_list)
    for num in new_list:
        sum += num
    return sum


if __name__ == "__main__":
    pass
