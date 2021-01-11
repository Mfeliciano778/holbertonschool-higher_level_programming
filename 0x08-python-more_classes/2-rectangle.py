#!/usr/bin/python3
'''Rectangle: An empty class called Rectangle'''


class Rectangle:
    '''rectangle - empty class'''
    def __init__(self, width=0, height=0):
        '''__init__ - instantiation with optional width and height'''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        '''width - getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width - setter for width'''
        self.__width = value

    @property
    def height(self):
        '''height - getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height - setter for height'''
        self.__height = value

    def area(self):
        '''area - returns the rectangle area'''
        return self.__height * self.__width

    def perimeter(self):
        '''perimeter - returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
