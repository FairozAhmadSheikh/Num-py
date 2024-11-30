"""
np.max(a)
np.min(a)
np.argmin(a)
np.argmax(a)
np.sqrt(a)
np.sin(a)
np.cos(a)
np.cumsum(a)
"""
import numpy as np

var=np.array([1,2,3,0,5,6,8,9])
print(np.max(var),"At Position",np.argmax(var))
print(np.min(var),"At Position",np.argmin(var))
print(np.sqrt(var))
print(np.cumsum(var))
print(np.sin(var))
print(np.cos(var))

# 2D Array max min

arr=np.array([[1,2,3],[4,5,6]])
print(np.max(arr,axis=0))
print(np.max(arr,axis=1))