#!/usr/bin/python3
'''Class Square'''


class Square:
    '''Square - defines size'''

    def __init__(self, size=0, position=(0, 0)):
        '''__init__ - Creates instance
           _Square_size: size of square'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(position) is not tuple or len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
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

    @property
    def position(self):
        '''position getter'''

        return self.__position

    @position.setter
    def position(self, value):
        '''position setter'''

        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        '''my_print - prints the square'''

        if self.__size == 0:
            print()
        else:
            for space in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for column in range(0, self.__size):
                    print("#", end="")
                print()
