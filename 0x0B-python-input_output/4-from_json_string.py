#!/usr/bin/python3
'''from_json_string'''
import json


def from_json_string(my_str):
    '''from_json_string - function returns an object rep by JSON string'''
    return json.loads(my_str)
