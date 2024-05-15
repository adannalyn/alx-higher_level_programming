#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for x in range(list_length):
        try:
            if x >= len(my_list_1) or x >= len(my_list_2):
                raise IndexError
            n1 = my_list_1[x]
            n2 = my_list_2[x]
            if not isinstance(n1, (int, float)):
                raise TypeError
            if not isinstance(n2, (int, float)):
                raise TypeError
            if n2 == 0:
                raise ZeroDivisionError
            result = n1 / n2
            result_list.append(result)
        except ZeroDivisionError:
            print(f"division by 0")
            result_list.append(0)
        except TypeError:
            print(f"wrong type")
            result_list.append(0)
        except IndexError:
            print(f"out of range")
            result_list.append(0)
        finally:
            continue
    return result_list
