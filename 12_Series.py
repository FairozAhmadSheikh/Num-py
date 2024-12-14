# import string as st
# import pandas as pd
# lst =[1,2,3,4,5,6,7,8,]
# lst2 =[9,8,7,6,5,4,3,2,]
# series=pd.Series(lst)
# series=pd.Series(lst2)
# df=pd.DataFrame({"LIST1":lst, "LIST2":lst2})
# print(df)

# from_dict={
#     "names":["sameer","hussain","insha","savleen","Fowkiyah"],
#     "roll_no":[30,34,16,14,22],
#     "score":[66,32,59,38,45],
# }

# pd2=pd.DataFrame(from_dict)
# print(pd2)


import pandas as pd

# Read the CSV file
dxx = pd.read_csv("C:/Users/habra/Desktop/archive/Titanic-Dataset.csv")
dxx.to_clipboard()

# Print the content of the DataFrame
print(dxx)

