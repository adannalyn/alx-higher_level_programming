#!/usr/bin/python3
def safe_print_division(a, b):
    results = 0
    try:
        result = int(a) / int(b)
        results = "{}".format(result)
        return results
    except ZeroDivisionError:
        pass
    finally:
        if results is None:
            print("Inside result: None")
        elif results is not None:
            print("Inside result: {}".format(results))
