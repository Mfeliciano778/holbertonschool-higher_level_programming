#!/usr/bin/python3
''''load_from_json_file'''
import json


def load_from_json_file(filename):
    '''load_from_json_file - creates an object from a json file'''
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
