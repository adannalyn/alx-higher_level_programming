#!/usr/bin/python3
def safe_print_division(a, b):
    results = 0
    try:
        if a == 0 or b == 0:
            return None
        else:
            result = int(a) / int(b)
            results = "{}".format(result)
            return results
    except ZeroDivisionError:
        pass
    finally:
        if results is not None:
            print("Inside result: {}".format(results))
