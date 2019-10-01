#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    result = []
    elem = 0
    for i in range(list_length):
        try:
            elem = my_list1[i] / my_list2[i]
        except IndexError:
            print("out of range")
            elem = 0
        except TypeError:
            print("wrong type")
            elem = 0
        except ZeroDivisionError:
            print("division by 0")
            elem = 0
        finally:
            result.append(elem)
    return result
