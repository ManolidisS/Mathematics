# Made by Spyridon Manolidis | 28/10/2023
from factorial import factorial

def binomial(n,r):
    '''Runs the mathematical binomial function, denoted by nCr'''
    x = (factorial(n))/((factorial(n-r))*(factorial(r)))
    x = int(x)
    return x