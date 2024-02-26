#!/usr/bin/python3
'''
Rectangle class definition
'''


class Rectangle():
    '''
    Rectangle class with width and height getter/setter methods
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' initializes the rectangle class '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        ''' width value getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width value setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' height value getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height value setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' calculates the area of the rectangle '''
        return self.height * self.width

    def perimeter(self):
        ''' calculates the perimeter of the rectangle '''
        if self.width ==  0 or self.height ==  0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)

    def __str__(self):
        ''' prints the rectangle '''
        if self.area() == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        ''' returns a string representation of the rectangle '''
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        ''' deletes the rectangle object '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' prints out which rectangle is bigger than which '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return (rect_1)
        if rect_2.area() > rect_1.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        ''' returns a new Rectangle instance with equal size '''
        return Rectangle(size, size)
