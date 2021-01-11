#!/usr/bin/python3
'''Rectangle: An empty class called Rectangle'''


class Rectangle:
    '''rectangle - empty class'''
    number_of_instances = 0
    print_symbol = '#'

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
            Rectangle.number_of_instances += 1

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

    def __str__(self):
        '''__str__ - prints the string rep of a rectangle'''
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rect += str(self.print_symbol)
            if i is not self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        '''__repr__ - prints the string rep of a rectangle'''
        width = str(self.__width)
        height = str(self.__height)
        return "Rectangle(" + width + ',' + height + ')'

    def __del__(self):
        '''__del__ - prints a message when an instance is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''bigger_or_equal - returns the biggest rectangle based on the area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1
