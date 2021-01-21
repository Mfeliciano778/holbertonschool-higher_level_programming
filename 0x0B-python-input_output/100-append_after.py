#!/usr/bin/python3
'''append_after'''


def append_after(filename="", search_string="", new_string=""):
    '''append_after - looks for string in file and inserts string after'''
    with open(filename, encoding='utf-8') as file:
        variable = file.readlines()
    index = 1
    file_list = list(variable)
    for line in range(0, len(file_list)):
        if search_string in file_list[line]:
            variable.insert(index, new_string)
            index += 1
        index += 1
    with open(filename, 'w', encoding='utf-8') as file_2:
        file_2.write("".join(variable))
