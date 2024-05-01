#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if isinstance(key, str):
        a_dictionary.pop(key, None)
    return a_dictionary


if __name__ == "__main__":
    pass
