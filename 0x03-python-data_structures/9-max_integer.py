#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # check if the list is empty
        return None
    else:
        max_num = my_list[0]  # set the first element as the initial maximum
        for num in my_list:
            if num > max_num:
                max_num = num
        return max_num
