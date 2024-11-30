import numpy as np 

arr=np.array([1,2,3,4,5,6])
print(arr)

x=[1,5,3,4,5,6]
y=np.array(x)
print(y)


# Zeros 
zer=np.zeros((4,4))
print(zer)

# Ones 
on=np.ones((4,4))
print(on)

# Sum of Two arrays 

# added=np.add(on,zer)
added=on+zer
print(added)


# Create N dimensional array

arr=np.array([1,2,3,4,5,6,7,8,9,10],ndmin=10)
print(arr)
print(arr.shape)

# Identity Matrix

at=np.eye(6)
print(at)

#Empty Array
em=np.empty(4)
print(em)

# Linspace
ar_lin=np.linspace(0,100,4)
print(ar_lin)