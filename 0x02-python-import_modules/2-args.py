#!/usr/bin/python3

import sys

args = sys.argv[1:]
arge = len(args)

if arge == 0:
    print("0 arguments.")
elif arge == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(arge))

counter = 1
for arg in range(arge):
    print(f"{counter}: {args[arg]}")
    counter += 1

if __name__ == "__main__":
    pass
