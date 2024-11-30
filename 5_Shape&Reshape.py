import numpy as np

var =np.array([[[2,4],[3,6],[5,6]]])
print(var)

# No of Dimensions
print(var.ndim)

# Blocks , rows and colomns given by shape
print(var.shape)

v1=np.array([[1,2,3,4,5],[1,3,4,5,6]])
v2=np.array([[5,4,3,2,1],[1,3,4,5,6]])
v3=v1*v2
print(v3)

# Reshaping

matr=np.array([1,2,3,4,5,6,7,8])
res=matr.reshape(4,2)
print(res)
print(res.ndim)

# 1D to 3D
matr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x3=matr.reshape(2,3,2)
print(x3)


# 3D TO 1D 

x4=x3.reshape(-1)
print(x4)