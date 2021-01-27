#!/usr/bin/python3
'''class Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle - class that inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''__init__ - instantiates width, height, x, y, and id'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width - getter of the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width - setter for width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''height - getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height - setter for height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''x - getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x - setter for x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''y - getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y - setter for y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''''area - function returns the area'''
        #might have to check if these exist
        return self.__width * self.__height

    def display(self):
        '''display - prints to stdout the rectangle using #'''
        for line in range(0, self.y):
            print("")
        for height in range(0, self.height):
            #print(" " * self.x, end="")
            for spaces in range(0, self.x):
                print(" ", end="")
            for width in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        '''__str__ returns the string rep of the rectangle instance'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''update - assigns an argument to each attribute'''
        argc = len(args)
        if args is not None and argc > 0:
            if args[0]:
                self.id = args[0]
            if argc >= 2:
                self.width = args[1]
            if argc >= 3:
                self.height = args[2]
            if argc >= 4:
                self.x = args[3]
            if argc >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict
