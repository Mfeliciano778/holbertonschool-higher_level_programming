#!/usr/bin/python3
'''class Base'''


class Base:
    '''Base - manage id attribute in all future classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''__init__ - instantiate id if it exists'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
