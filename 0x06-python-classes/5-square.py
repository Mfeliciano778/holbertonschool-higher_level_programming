#!/usr/bin/python3
'''Class Square'''


class Square:
    '''Square - defines size'''

    def __init__(self, size=0):
        '''__init__ - Creates instance
           _Square_size: size of square'''

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''area - returns the area of the square'''

        return self.__size ** 2

    @property
    def size(self):
        '''size - getter for size'''

        return self.__size

    @size.setter
    def size(self, value):
        '''size - setter for size'''

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        '''my_print - prints the square'''

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
