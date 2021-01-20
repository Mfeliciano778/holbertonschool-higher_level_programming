#!/usr/bin/python3
'''class Student'''


class Student:
    '''Student - defines what a student is'''

    def __init__(self, first_name, last_name, age):
        '''__init__ - instantiates attributes of a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''to_json - retrieves dictionary representation of a student'''
        new_dict = {}
        if type(attrs) is list:
            for key in attrs:
                if type(key) is str:
                    try:
                        new_dict[key] = self.__dict__[key]
                    except:
                        pass
            return new_dict
        return vars(self)

    def reload_from_json(self, json):
        '''relaod_from_json - replaces all attributes of an instance'''
        for key in json:
            setattr(self, key, json[key])
