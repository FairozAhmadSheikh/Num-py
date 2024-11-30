import numpy as np
v1=np.array([1,9,3,4,5,8,0])

# Using Positive index
print(v1[5])

# Using Negative index 
print(v1[-2])  # second last element 

# 2D array

v2=np.array([[1,2,3],[4,5,6]])
print(v2[1,2])  # gives last elemet


#3D Array

v3=np.array([[[1,2,3],
              [1,2,3],
              [3,2,1]]])

print(v3[0,2,2])  # Prints last element