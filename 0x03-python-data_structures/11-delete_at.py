#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    if idx < len(my_list) and idx >= 0:
        del my_list[idx]
        del new_list[idx]
    return new_list
