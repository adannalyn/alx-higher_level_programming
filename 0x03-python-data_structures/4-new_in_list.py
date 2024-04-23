#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_liste = my_list.copy()
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_liste[idx] = element
    return new_liste


if __name__ == "__main__":
    pass
