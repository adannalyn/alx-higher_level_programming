#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            formatted = "{:d}".format(value)
            print(formatted)
            return True
        else:
            return False
    except IndexError:
        pass
