from c_matrix import c_matrix
from e_matrix import e_matrix
from dimensions import dimensions

def dot_product(m1,m2): 
  try: 
    if (dimensions(m1)[1] == dimensions(m2)[0]):
      pass
  except: 
    raise Exception("Ensure parameters are matricies and have the compatable dimensions.") 
  else:
    x = c_matrix(dimensions(m1)[0],dimensions(m2)[1])
    y = 0
    for i in range(len(m1)): # Haven't used dimensions() to make it faster; I'm going to be using many for loops anyways so I don't want the extra ones it uses.
      for j in range(len(m1)):
        for k in range(len(m1[i])): # At first it might seem weird using three for loops, but I'm doing it because when multiplying matricies, you have to 1st row * 1st column, 1st row * 2nd column, 2nd row * 1st column, etc. as well as have a for loop counting each element of the matrix so you can multiply it with the corresponding one on the other matrix.
          y = y + (m1[i][k] * m2[k][j])
        e_matrix(x,(i+1),(j+1),y)
        y = 0
    return x
