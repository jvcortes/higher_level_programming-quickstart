#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{:d} is".format(number),
      "zero" if number == 0 else
      "positive" if number > 0
      else "negative")
