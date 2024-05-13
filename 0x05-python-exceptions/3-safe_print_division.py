#!/usr/bin/python3
def safe_print_division(a, b):
    results = 0
    try:
        if a == 0:
            return None
        elif b == 0:
            return None
        else:
            result = int(a) / int(b)
            results = "{}".format(result)
            return results
    except IndexError:
        pass
    finally:
        if results is None:
            return None
        else:
            print("Inside result: {}".format(results))
