def dimensions(matrix):
    '''
    Returns an array with element 1 being the no. of rows and element 2 being the no. of columns.
    '''
    x = [0,0]
    x[0] = len(matrix)
    y = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        y = y + 1
    y = int(y/len(matrix))
    x[1] = y
    return x
