#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list1[i] / my_list2[i])
        except IndexError:
            print("out of range")
            result.append(0)
            continue
        except TypeError:
            print("wrong type")
            result.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
            continue
    return result
