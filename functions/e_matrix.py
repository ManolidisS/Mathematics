def e_matrix(matrix,m,n,x): 
  try: 
    matrix[m-1][n-1] = x 
    return matrix 
  except Exception as err: 
    raise Exception("Function e_matrix() has failed. Check the inputs.\nError: " + str(err))
