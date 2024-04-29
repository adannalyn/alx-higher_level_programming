#!/usr/bin/python3

def search_replace(my_list, search, replace):
    #my_list = [replace if num == search else num for num in my_list]

    new_list = []
    for num in range(len(my_list)):
        if num == index(search):
            new_list.append(replace)
        else:
            new_list.append(num)
    return new_list


if __name__ == "__main__":
    pass
