#!/usr/bin/python3
'''class Square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square - inherits and instanstiates Rectangle'''

    def __init__(self, size):
        '''__init__ - instanstiates size'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''__str__ - function returns the string representation of a square'''
        return "[Square] {}/{}".format(self.__size, self.__size)
