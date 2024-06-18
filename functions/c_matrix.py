def c_matrix(m,n):
  '''Creates a matrix with m rows and n columns'''
  matrix = []
  for i in range(m):
    row_matrix = []
    for j in range(n):
      row_matrix.append(0)
    matrix.append(row_matrix)
  return matrix