#!/usr/bin/python3
'''add attribute'''


def add_attribute(self, name, value):
    '''add attribute'''
    if hasattr(self, "__dict__") is False:
        raise TypeError("can't add new attribute")
    self.__setattr__(name,  value)
