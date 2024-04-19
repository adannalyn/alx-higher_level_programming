#!/usr/bin/python3

import sys

args = sys.argv[1:]
arge = len(args)

if arge == 0:
    print("0 arguments.")

else:
    print("{} arguments:".format(arge))
    counter = 1

    for arg in args:
        print(f"{counter}: {arg}")
        counter += 1
