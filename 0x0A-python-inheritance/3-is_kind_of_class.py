#!/usr/bin/python3
'''Function returns boolean if the object is an instance of a class'''


def is_kind_of_class(obj, a_class):
    '''is_kind_of_class returns true/false if object is an instance of a class
    '''
    return issubclass(type(obj), a_class)
