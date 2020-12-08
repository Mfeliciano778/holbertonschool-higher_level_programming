#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lst_dgt = number % 10
else:
    lst_dgt = -(abs(number) % 10)

if abs(lst_dgt) > 5:
    print("Last digit of", end=" ")
    print("{:d} is {:d} and is greater than 5".format(number, lst_dgt))
elif abs(lst_dgt) == 0:
    print("Last digit of", end=" ")
    print("{:d} is {:d} and is zero".format(number, lst_dgt))
else:
    print("Last digit of", end=" ")
    print("{:d} is {:d} and is less than 6 and not 0".format(number, lst_dgt))
