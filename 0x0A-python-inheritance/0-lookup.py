#!/usr/bin/python3
'''lookup function puts all info on an object in a dict'''


def lookup(obj):
    '''lookup - puts all attributes and methods of an obj in a dict'''
    return dir(obj)
