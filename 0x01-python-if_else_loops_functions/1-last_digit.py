#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    numbers = number % -10
else:
    numbers = number % 10
if numbers > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, numbers))
elif numbers < 6 and numbers != 0:
	print("Last digit of {} is {} and is less than 6 and not 0".format(number, numbers))
elif numbers == 0:
    print("Last digit of {} is {} and is 0".format(number, numbers))
