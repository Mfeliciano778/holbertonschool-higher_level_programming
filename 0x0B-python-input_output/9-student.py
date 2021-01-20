#!/usr/bin/python3
'''class Student'''


class Student:
    '''Student - defines what a student is'''

    def __init__(self, first_name, last_name, age):
        '''__init__ - instantiates attributes of a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''to_json - retrieves dictionary representation of a student'''
        return vars(self)
