from math import sqrt

def magnitude2d(x,y):
    '''Returns the magnitude of a 2D vector'''
    a = sqrt((x**2)+(y**2))
    if (a % 1) != 0:
        return a
    else:
        return int(a)