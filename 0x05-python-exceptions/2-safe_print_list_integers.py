#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                print(element, end="")
                count += 1
    except IndexError:
        return
    print()
    return count
