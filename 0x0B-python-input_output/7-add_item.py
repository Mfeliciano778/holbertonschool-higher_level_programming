#!/usr/bin/python3
'''add_item - script add arguments to a python list then adds it to file'''
import json, sys
loads = __import__('6-load_from_json_file').load_from_json_file
saves = __import__('5-save_to_json_file').save_to_json_file

try:
    py_list = loads("add_item.json")
except:
    py_list = []

for index in range(1, len(sys.argv)):
    py_list.append(sys.argv[index])

saves(py_list, "add_item.json")
