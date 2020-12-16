#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for num in my_list:
            if max_int < num:
                max_int = num
        return max_int
    else:
        return None
