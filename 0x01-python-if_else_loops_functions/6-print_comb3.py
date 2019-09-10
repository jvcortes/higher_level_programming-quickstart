#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print("{:d}".format(i), end='')
            if i != 8 or j != 9:
                print("{:d}, ".format(j), end='')
            else:
                print("{:d}".format(j))
