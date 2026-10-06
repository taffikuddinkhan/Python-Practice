import pandas as pd # importing pandas library and giving it a early as / temporary name pd

'''
- inserting value ================================================================================================================================================

- adding columns in a dataset using insert method : df.insert(loc,"column name",some data) , loc - location, where you want to insert the column
- adding column directly : df['column'] = df['column'*formula] / you list or object

- updating values ================================================================================================================================================

-loc[] you can access a specific cell by this 
-loc[row_index,"column value"] = new value / the value you want to update  , here loc[] means location 

- removing / delete column ========================================================================================================================================

-df.drop(columns=["column name"],inplace=True)  ,  in this inplace = True means that the original dataframe will be affected directly , if inplace is False then it will provide you a copy of the dataframe

'''

# read data from csv file
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Data Science Roadmap Preparataion Materials\Projects\Employee.csv') # csv - comma separated file

# adding columns in a dataset using insert method
df.insert(5,"salary",df["Age"]*1000) # added a new column named salary , calculated by the  "candidate age * 1000"  formula  
print(df.head()) # printing first 5 rows 

# adding column in a adataset directly
df["Employee Id"] = range(1,1+len(df))
print(df.head())
print()

# updating a aparticular value  , updating a single cell value in a column
df.loc[0,'salary'] = 40000 # updating salary columns first row , and the row starts from 0 
print(f'After updating the salary columns first value \n\n {df.head()}')
print()

# updating salary
df["salary"] = df["salary"] + 1 # updating an entire column
print(f'After updating the salary by increasing 1 \n\n {df.head()}')
print()

# Deleting a single column                                          [ in this ,   "inplace = True"  means that the original dataframe will be affected directly ]
df.drop(columns=["PaymentTier"],inplace=True)
print(f'After deleting the column PaymentTier \n\n {df.head()}')
print()

# deleting multiple columns
df.drop(columns=["JoiningYear","EverBenched","LeaveOrNot"],inplace=True)
print(f'After deleting the column JoiningYear","EverBenched","LeaveOrNot"  \n\n {df.head()}')
print()



