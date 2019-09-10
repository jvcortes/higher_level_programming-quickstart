#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number),
      "{:d} and is".format(number % 10),
      "zero" if number % 10 == 0 else
      "greater than five" if number % 10 > 5
      else "less than 6 and not 0")
