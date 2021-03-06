#!/usr/bin/python3
'''Class Square'''


class Square:
    '''Square - defines size'''

    def __init__(self, size=0):
        '''__init__ - Creates instance
           _Square_size: size of square'''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''area - returns the area of the square'''

        return self.__size ** 2
