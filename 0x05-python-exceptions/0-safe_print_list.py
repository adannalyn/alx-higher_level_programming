#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            element = my_list[i]
            count += 1
            print(element, end="")
    except IndexError:
        pass
    print()
    return count
