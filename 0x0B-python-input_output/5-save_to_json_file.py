#!/usr/bin/python3
'''save_to_json_file'''
import json


def save_to_json_file(my_obj, filename):
    '''save_to_json_file - wrties an object to a file using Json rep'''
    with open(filename, mode='w', encoding='utf-8') as file:
        string = json.dumps(my_obj)
        file.write(string)
