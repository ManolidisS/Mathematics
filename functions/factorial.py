from isInt import isInt

def factorial(n):
    '''
    Runs the mathematical factorial function, denoted by n!\n
    Restricted to (n ∈ Z) ∧ (1 ≤ n)
    '''
    if not isInt(n):
        raise Exception("n is not an integer.")
    x = 1
    for i in range(n):
        x = x*(i+1)
    return int(x)
