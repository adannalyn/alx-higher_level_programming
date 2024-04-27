#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new = my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
    elif idx > 0 or idx <= len(my_list):
        del new[idx]
        return new


if __name__ == "__main__":
    pass
