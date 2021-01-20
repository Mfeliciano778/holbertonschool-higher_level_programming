#!/usr/bin/python3
'''append_write'''


def append_write(filename="", text=""):
    '''append_write - appends to a file and returns the  number of
    characters written'''
    with open(filename, mode='a', encoding='utf-8') as file:
        characters = file.write(text)
    return characters
