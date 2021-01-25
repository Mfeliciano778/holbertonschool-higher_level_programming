#!/usr/bin/python3
'''class Base'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''to_json_string - returns Json string representation of
        list_dictionaries'''
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save_to_file - writes Json string rep to a file'''
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8')
        as file:
                string = Base.to_json_string(new_list)
                file.write(string)

    @staticmethod
    def from_json_string(json_string):
        '''from_json_string - returns the list of Json string rep'''
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create - returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dumdum = cls(3, 3, 0, 0)
        else:
            dumdum = cls(3, 0, 0)
        dumdum.update(**dictionary)
        return dumdum

    @classmethod
    def load_from_file(cls):
        '''load_from_file - returns a list of instances'''
        new_list = []
        try:
            with open("{}.json".format(cls.__name__), encoding="utf-8")
            as file:
                instances = file.read()
        except:
            return new_list
        instances = cls.from_json_string(instances)
        for instance in instances:
            new_list.append(cls.create(**instance))
        return new_list
