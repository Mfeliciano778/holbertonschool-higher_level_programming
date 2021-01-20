#!/usr/bin/python3
'''write_file'''


def write_file(filename="", text=""):
    '''write_file - function writes specified text to a specified file'''
    with open(filename, mode='w', encoding='utf-8') as file:
        characters = file.write(text)
    return characters
