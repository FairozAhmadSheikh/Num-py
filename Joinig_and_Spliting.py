# Joining means putting contents of two arrays are more than two into one single array
import numpy as np

# 1D ArrAY
a=np.array([1,2,3,4,4,5,6,7])
a1=np.array([1,2,3,4,4,5,6,7])
conc=np.concatenate((a,a1))
print(conc)

#2d array
a2=np.array([[1,2,3,4],
             [5,6,7,9]])
a3=np.array([[1,2,3,4],
             [5,6,7,8]])

a4=np.concatenate((a2,a3),axis=1)
print(a4)

# Join Using Stack 

s1=np.array([[1,2,3],[4,5,8]])
s2=np.array([[1,2,3],[4,5,7]])
s4=np.array([[7,8,8],[9,7,2]])

s3=np.stack((s1,s2),axis=0)
print()
print(s3)

# Horizontal Stack
print(np.hstack((s1,s2)))
# Vertical Stack
print(np.vstack((s1,s2)))
# On Height basis
print(np.dstack((s1,s2,s4)))


# Splitting An array
# Breaking array into parts

s9=np.array([1,2,3,4,5,6,7,8,9])
s8=np.array_split(s9,3)
print("Spliting starts from here")
print("Orignal Array: ",s9)

print("Splitted Array : ",s8)
print(s8[0],s8[1],s8[2])

# 2D Array Splitting

s32=np.array([[1,2,3],[4,5,6],[7,8,9]])
s31=np.array_split(s32,3)
print(s31)