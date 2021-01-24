#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square - class that inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''__init__ - instantiate size, x, y, and id'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''__str__ returns the string rep of the square instance'''
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
        self.width)

    @property
    def size(self):
        '''size - getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''size - setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update - assigns attributes to square'''
        argc = len(args)
        if args is not None and argc > 0:
            if args[0]:
                self.id = args[0]
            if argc >= 2:
                self.size = args[1]
            if argc >= 4:
                self.x = args[2]
            if argc >= 5:
                self.y = args[3]
        else:
            for key,value in kwargs.items():
                setattr(self, key, value)