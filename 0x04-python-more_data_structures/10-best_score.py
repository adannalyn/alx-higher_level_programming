#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    value = list(a_dictionary.values())
    key = list(a_dictionary.keys())

    return key[value.index(max(value))]


if __name__ == "__main__":
    pass
