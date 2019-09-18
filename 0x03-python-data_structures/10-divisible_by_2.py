#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        is_div = []
        for i in my_list:
            if not abs(i) % 2:
                is_div.append(True)
            else:
                is_div.append(False)
        return is_div
