#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                num_1 = my_list_1[i]
                num_2 = my_list_2[i]
                if not isinstance(num_1, (int, float)) or not isinstance(num_2, (int, float)):
                    raise TypeError
                if num_2 == 0:
                    raise ZeroDivisionError
                result = num_1 / num_2
                result_list.append(result)
            except IndexError:
                print("out of range")
                result_list.append(0)
            except TypeError:
                print("wrong type")
                result_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
    finally:
        return result_list
