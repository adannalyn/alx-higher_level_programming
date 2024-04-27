#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new = my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
<<<<<<< HEAD
    else:
        new_list = my_list[:idx] + my_list[idx + 1:]
        return new_list
=======
    elif idx > 0 or idx <= len(my_list):
        del new[idx]
        return new
>>>>>>> 053ae6ab0fe8634b88db167e3a0475b71d1d96b2


if __name__ == "__main__":
    pass
