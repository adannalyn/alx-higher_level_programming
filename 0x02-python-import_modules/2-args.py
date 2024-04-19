#!/usr/bin/python3

import sys

counter = 0

for arg in sys.argv:
    if len(arg) > 1:
        print("{}: {}".format(counter, arg))
        counter += 1
    gielse:
        print("{}".format(len(arg)))
