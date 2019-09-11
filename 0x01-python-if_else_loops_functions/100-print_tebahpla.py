#!/usr/bin/python3
mayus = True
for i in range(122, 96, -1):
    mayus = not mayus
    print("{}".format(chr(i - 32) if mayus else chr(i)), end='')
