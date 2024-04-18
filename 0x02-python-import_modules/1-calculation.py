#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

adde = add(a, b)
sube = sub(a, b)
mule = mul(a, b)
dive = div(a, b)

print("{} + {} = {}".format(a, b, adde))
print("{} - {} = {}".format(a, b, sube))
print("{} * {} = {}".format(a, b, mule))
print("{} / {} = {}".format(a, b, dive))

if __name__ == "__main__":
    add(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)
