#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} ".format(number))
if (number % 10) > 5:
    print("is {:d} and is greater than 5".format(number % 10))
elif (number % 10) == 0:
    print("is {:d} and is zero".format(number % 10))
elif (number % 10) < 6 and not 0:
    print("is {:d} and is less than 6 and not 0".format(number % 10))
else:
    print("Not a number")
