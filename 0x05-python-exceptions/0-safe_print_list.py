#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in my_list[:x]:
        try:
            print("{}".format(i), end='')
            c += 1
        except IndexError:
            break
    print()
    return c
