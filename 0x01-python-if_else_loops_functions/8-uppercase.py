#!/usr/bin/python3

def uppercase(str):
    result = ""
    for words in str:
        if ord('a') <= ord(words) <= ord('z'):
            results = chr(ord(words) - 32)
        else:
            results = words
        result += results
    print('{}'.format(result), end="\n")
