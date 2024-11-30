# Out of syallabus
import numpy as np
var1=np.array([1,2,3,4,5])
var2=np.array([1,2,3,4,5])
varz=var1+var2
print(varz)

# If number of elemts are not equal it causes a broadcast error 
# Two rules of broadcasting is that 
"""
1: No of elements should be equal 
2: in case not equal it should be like arr1=(3 X 1 ) and arr2 =(1 X 3 ) where one dimesion is equal to one 
Example below:
"""

var1=np.array([1,2,3])  # 1 x 3 
var2=np.array([[1],[2],[3]])   # 3 X 1
c=var1+var2   # 3 X 3   MAX ELEMTS OF VAR1 AND VAR 2 
print(c)