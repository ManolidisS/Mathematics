def e_matrix(matrix,m,n,x):
  '''Edits the element of a given matrix in row m and column n to give it a value of x'''
  matrix[m-1][n-1] = x
  return matrix