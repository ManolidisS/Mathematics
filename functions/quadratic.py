from math import sqrt

def quadratic(a,b,c):
    '''Uses the quadratic formula on the quadratic equation ax^2 + bx + c = 0'''
    if ((b**2)-(4*a*c)) > 0:
        x = [(((-1*b)+sqrt((b**2)-(4*a*c))/(2*a))), (((-1*b)-sqrt((b**2)-(4*a*c))/(2*a)))]
    elif ((b**2)-(4*a*c)) == 0:
        x = [(((-1*b)+sqrt((b**2)-(4*a*c))/(2*a))),]
    elif ((b**2)-(4*a*c)) < 0:
        x = [((-1*b)/(2*a))+"+"(sqrt(-1*((b**2)-(4*a*c))))+"i",((-1*b)/(2*a))+"-"(sqrt(-1*((b**2)-(4*a*c))))+"i"]    
    return x