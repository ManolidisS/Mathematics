from math import sqrt

def magnitude3d(x,y,z):
    '''Returns the magnitude of a 3D vector'''
    a = sqrt((x**2)+(y**2)+(z**2))
    if (a % 1) != 0:
        return a
    else:
        return int(a)