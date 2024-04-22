#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx not in my_list:
        return None
    elif idx in my_list:
        index = my_list.index(idx)
        return index


if __name__ == "__main__":
    pass
