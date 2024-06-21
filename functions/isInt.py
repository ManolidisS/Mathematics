def isInt(x):
    '''
    Checks to see whether a function is an integer or not.\n
    Returns true or false.
    '''
    try:
        if x%1 == 0:
            return True
        else:
            return False
    except:
        return False
