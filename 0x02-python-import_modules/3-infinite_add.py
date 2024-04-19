#!/usr/bin/python3

import sys

summ = sum(int(i) for i in sys.argv[1:])
print("{}".format(summ))

if __name__ == "__main__":
    pass
