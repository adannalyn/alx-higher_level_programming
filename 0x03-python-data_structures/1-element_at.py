#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx not in my_list:
        return None
    elif idx in my_list:
        indx = my_list[idx]
        return indx


if __name__ == "__main__":
    pass
