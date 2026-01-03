import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("all installed successfully")
matcars=pd.read_csv(r"C:\Users\ankit\Downloads\archive\Iris.csv")
# Always use raw strings (r"...") for Windows file paths
print(matcars.head(10))  
# .head for print 5 rows and .tail to print 10 rows
#to print whole datasets we use .info ex- matcars.info()
print(matcars.describe())  
print(matcars.columns)   #to show all the columns name
print(matcars.shape)  #to show total number of rows & columns
res = sns.barplot(x="Species", y="SepalLengthCm", data=matcars)
plt.show()

