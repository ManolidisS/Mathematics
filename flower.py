# This was meant to start off as a small quick gimmick and took me 2 hours, nice.
# Spyros da Best - June 2024.
# I don't know if you can tell what I'm doing because I prioritised less line over readability
# Basically I started by trying to draw a quadratic graph in turtle and eventually got the result I was looking for
# I was gonna explain this but I made it so confusing I already forgot so good luck
# Yeah but basically that's it, and arctan is used on the gradient of the tangent (2x, the derivative of x^2, the quadratic), 
# which I think eventually became width, and arctan finds the angle from the x axis to rotate.
# also I have to keep both the angle from the x axis and the last angle used so I know how much to rotate
# relative to the last angle (I hope makes sense)
'''
before I made it unreadable it was
num = 50 # Number of times to break up the curve; bigger = slower but more accurate
maxima = 1 # Maximum value to reach on quadratic graph
inc = maxima/num

from math import *
from turtle import *

speed(speed=1000)

def f(x):
    return x**2

def fprime(x):
    return 2*x

def tangent(x1):
    y1 = f(x1)
    m = fprime(x1)
    return [x1,y1,m]

ang = [0,0]

for i in range(num):
    z = tangent((i+1)*inc)
    ang[1] = ((360*(atan((z[2]))))/(2*pi))
    turn = ang[1]-ang[0]
    left(turn)
    forward(10)
    ang[0] = ang[1]

exitonclick()
'''
# From that point onwards I just did it again with a 180 deg rotation so it forms a petal, and
# just did lots of loops with my new function to make a flower.


from math import *
from turtle import *

speed(speed=1)

def petal(width,num,size):
    ang = [0,0]

    for i in range(num):
        ang[1] = ((360*(atan(width*((i+1)*(1/num)))))/(2*pi))
        left(ang[1]-ang[0])
        forward(size)
        ang[0] = ang[1]
    left(180)
    for i in range(num):
        ang[1] = ((360*(atan(width*((i+1)*(1/num)))))/(2*pi))
        left(ang[1]-ang[0])
        forward(size)
        ang[0] = ang[1]

fillcolor("pink")
for i in range(4):
    begin_fill()
    for i in range(4):
        petal(1,50,5)
        left(45)
    end_fill()
    left(22.5)

exitonclick()