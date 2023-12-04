#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None

    if len(my_list) == 1:
        return my_list[0]

    biggest = my_list[0]
    for i in range(1,len(my_list)):
        if biggest < my_list[i]:
            biggest = my_list[i]
    return biggest
