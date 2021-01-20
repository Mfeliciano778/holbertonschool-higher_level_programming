#!/usr/bin/python3
'''read_file'''


def read_file(filename=""):
    '''read_file - reads from a file and prints the contents'''
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
