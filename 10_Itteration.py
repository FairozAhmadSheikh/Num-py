import numpy as np

# Iteration of arrays using loops and nditer()
# 1d array
a=np.array([1,2,3,4,5,6,7,8,9])

for val in a :
    print(val,end="*")
print() 
# 2D Array
a2=np.array([[1,2,3,4,5],[6,7,8,9,10]])

for val in a2:
    for internal in val :
        print(internal)
    
#3D Array

a3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a3)
print()
for i in a3:
    for j in i :
        for k in j :
            print(k,end="")
            
#USING nditer Function
for i in np.nditer(a3):
    print(i)

# # Change dtype using nditer 
# Here we use buffer for temperory data storange and convert in into string in temp memory
for i in np.nditer(a3,flags=['buffered'],op_dtypes="S"):
    print(i)
    
    
    
"""
ndenumerate Function gives 
Index and value 

"""

f4=np.array([[[6,7,8,9],[1,2,3,4],[5,6,6,8]]])
for i,d in np.ndenumerate(f4):
    print("For index : ",i,"Value is = ",d)