def squareroot(x:float,n:int=4)->float:
    '''
    Returns the (approximated) square root as a float for any given number that is either real or imaginary (cannot be complex).
    The variable n is the number of iterations and is automatically set to 4. Increasing it will yield a more accurate result, at the expense of more processing.
    '''
    if x > 0:
        # Finding a, the closest integer square root
        a = 1
        while abs(x - a**2) >= abs(x - (a+1)**2):
            a = a + 1
        # Iterative process for increasing accuracy
        z= [a, x-a**2, 2*a]
        for i in range(n):
            a = z[0] + ((z[1])/(z[2]))
            z= [a, x-a**2, 2*a]
        return z[0] + ((z[1])/(z[2]))
    
    elif x == 0:
        return 0
    
    elif x < 0:
        x = -x

        # Finding a, the closest integer square root
        a = 1
        while abs(x - a**2) >= abs(x - (a+1)**2):
            a = a + 1
        # Iterative process for increasing accuracy
        z= [a, x-a**2, 2*a]
        for i in range(n):
            a = z[0] + ((z[1])/(z[2]))
            z= [a, x-a**2, 2*a]
        return complex(0, z[0] + ((z[1])/(z[2])))