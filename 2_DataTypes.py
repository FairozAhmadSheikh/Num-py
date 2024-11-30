import numpy as np 

var=np.array([1,2,3,4,5,6,7,8,9,])
print(var.dtype)
print(var)

# Type casting 
x=np.array([1,2,3,4])
print(x.dtype)

new=x.astype(float)
print(new.dtype)
print(new)
