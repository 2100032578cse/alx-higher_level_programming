#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
newn = number % 10
if number < 0:
    newn = (-number % 10) * -1
if newn > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, newn))
elif newn == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, newn))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, newn))
