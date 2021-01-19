#!/usr/bin/python3
'''class BaseGeometery'''


class BaseGeometry:
    '''BaseGeometry - does geometry'''

    def area(self):
        '''area - raises exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''integer_validator - validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
