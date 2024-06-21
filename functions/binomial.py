from isInt import isInt
from factorial import factorial

def binomial(n,r):
    '''
    Runs the mathematical binomial function, denoted by nCr
    '''
    if r > n:
        raise Exception("n < r. Cannot compute negative factorials.")
    elif (not isInt(n)) or (not isInt(r)):
        raise Exception("ensure n & r are integers.")
    else:
        x = (factorial(n))/((factorial(n-r))*(factorial(r)))
        return int(x)
