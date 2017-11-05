__author__ = 'Sharad Durgawad'

import math

def Area_Circle(r):
    """
    :param r: Radius of a Circle
    :return: Area of Circle
    """
    area = r**2 * math.pi
    return area

print("\n Enter the list of Shapes: ")

print("\n 1. Triangle \n 2. Rectangle \n 3. Square \n 4. Circle \n 5. Quit \n")

option = int(input('Enter the option: '))

if(option == 1):
    h = int(input('Enter the height: '))
    b = int(input('Enter the base: '))
    area = float((h*b)/2)
    print("\n Area of Triangle = %f" % area)

elif (option == 2):
    l = int(input('Enter the length: '))
    w = int(input('Enter the width: '))
    area = float(l*w)
    print("\n Area of Rectangle = %f" % area)

elif (option == 3):
    s = int(input('Enter the side: '))
    area = float(s*s)
    print("\n Area of Square = %f" % area)

elif (option == 4):
    r = int(input('Enter the radius: '))
    print("\n Area of Circle = %f" % Area_Circle(r))

elif (option == 5):
    exit()
