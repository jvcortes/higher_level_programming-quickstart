#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    for n in set(my_list):
        x += n
    return x
