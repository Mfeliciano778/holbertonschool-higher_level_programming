#!/usr/bin/python3
'''class_to_json'''


def class_to_json(obj):
    '''class_to_json - function that returns dictionary description for Json
    serialization of an object'''
    return vars(obj)
