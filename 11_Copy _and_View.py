import numpy as np

a1=np.array([1,2,3,4,0,5,6])
a1[0]=9
# Makes a copy and owns the data now 
a2=a1.copy()
print(a2)
# Views data does not own data
print(a1.view())