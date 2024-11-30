import numpy as np

"""
a+b = np.add(a,b)
a-b = np.subtract(a,b)
a*b = np.multiple(a,b)
a/b = np.divide(a,b)
a%b = np.mod(a,b)
a**b = np.power(a,b)
1/a = np.reciprocal(a)
"""
# Add
var=np.array([1,2,3,4])
added=np.add(var,6)
print(added)

# Multiplication
var=np.array([1,2,3,4])
multiplied=np.multiply(var,6)
print(multiplied)

# Divide
var=np.array([1,2,3,4])
divided=np.divide(var,6)
print(divided)

# Modulus Gives reminder
var=np.array([1,2,3,4])
modlus=np.mod(var,2)
print(modlus)

# Floor Divison 
var=np.array([1,2,3,4])
floor=var//2
print(floor)

# Power 
var=np.array([1,2,3,4])
power=var**2
print(power)


# Reciprocal
var = np.array([1, 2, 3, 4, 5])
recp = np.reciprocal(var.astype(float))  # Ensure elements are treated as float
print(recp)


