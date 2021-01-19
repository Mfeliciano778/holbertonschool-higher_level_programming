#!/usr/bin/python3
'''inherits_from checks if obj is an instance indirectly or directly'''


def inherits_from(obj, a_class):
    '''inherits_from checks if obj is an instance indirectly or directly'''
    return issubclass(type(obj), a_class) and type(obj) != a_class
