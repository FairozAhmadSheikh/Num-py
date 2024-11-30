# rand(), randn(), randf(),randint()
import numpy as np

# Generate Number Btween 0 and one # rand()   only positives
n1=np.random.rand()
print(n1)

# randn() #Generates a number  close to zero positive and negative
n2=np.random.randn()
print(n2)

# ranf() # returns [0.0 to 1.0) where 1.0 is excluded
n3=np.random.ranf()
print(n3)

# randint()  # Generates number between a given range
# Takes three inputs first minimum parameter , second parameter as maximum parameter, number of  total values to be generated 

n4=np.random.randint(5,20,10)
print(n4)