#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
    for i in my_list:
        if idx >= len(my_list) or idx < 0:
            return my_list
        elif i == idx:
            my_list[i] = element
            return my_list
    return None
