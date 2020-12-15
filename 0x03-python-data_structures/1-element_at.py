#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list:
        for i in my_list:
            if idx > len(my_list) or idx < 0:
                return None
            elif my_list[i] == idx:
                return my_list[idx]
        return None
