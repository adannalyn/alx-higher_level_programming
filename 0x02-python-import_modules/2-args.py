#!/usr/bin/python3

import sys

print(len(sys.argv[1:]), "arguments:")

arg = len(sys.argv)

counter = 1

for args in range(1, arg):
    if args > 0:
        print(f"{counter}: {sys.argv[args]}")
        counter += 1
    elif args == 0:
        print("0 arguments.")
