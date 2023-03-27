#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                if divisor != 0:
                    result_list.append(dividend / divisor)
                else:
                    print("division by 0")
                    result_list.append(0)
            else:
                print("wrong type")
                result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            pass
    return result_list
