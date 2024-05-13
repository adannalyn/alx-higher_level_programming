#!/usr/bin/python3
def safe_print_division(a, b):
    results = 0
    try:
        if a == 0 or b == 0:
            return
        else:
            result = int(a) / int(b)
            results = "{}".format(result)
            return results
    except IndexError:
        pass
    finally:
        print("Inside result: {}".format(results))
