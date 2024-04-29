#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list = [replace if num == search else num for num in my_list]
    return my_list


if __name__ == "__main__":
    pass
