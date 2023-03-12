#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []  # initialize the new list
    for num in my_list:
        if num % 2 == 0:  # check if the number is divisible by 2
            result.append(True)
        else:
            result.append(False)
    return result
