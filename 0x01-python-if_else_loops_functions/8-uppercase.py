#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            ch = chr(ord(i) - 32)
        else:
            ch = i
        print("{}".format(ch), end='')
    print("")
