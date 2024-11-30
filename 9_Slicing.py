# obtaining particular peice of an array 
import numpy as np

v=np.array([3,2,5,6,7,3,2])
print(v[:5]) # Starting to 5th index 

print(v[0:len(v)+1:1]) # start from 0 end on last index and step size 1


# 2d array

v2=np.array([[1,2,3],[4,4,5]])

print(v2[1,0:3]) # 4 4 5 

#3D ARRAY
v3=np.array([[[1,2,4],[3,4,6],[4,5,9]]])
print(v3[0,1,::]) # 3 4 6