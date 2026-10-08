import pandas as pd # importing pandas library and giving it a early as / temporary name pd

'''
- isnull() used to find that the values are missing or not , and give result in boolean format
- dropna(axis=0 , inplace = True) used to delete null values , if the axis is 0 then it will perform operation on rows and if it is 1 then operation in columns
- fillna(value , inplace = True ) filling a default value where null present

- Interpolution ==============================================================================================================================================================

1- preserve data integrity [ predict realestic numbers and replace with them with the null values ] 
2- smooth trends 
3- Avoid data loss

- use interpolate() method to perform this type of operations
- method - linear , polynomial , time 
- use only when works in data series like time and series , numeric data with trends , no need to delete the total row just fill it with a estimated value

'''

# read data from csv file
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Data Science Roadmap Preparataion Materials\Employee_null.csv') # csv - comma separated file 
print(df.isnull()) # return a boolean value of each column that null value is present or not 
print(df.isnull().sum()) # return the sum or umber of null values in a column

# handling null values ======================================================================================================================================================

df.dropna(axis=0,inplace=True) # deleting the null values present in the row
df.fillna(0,inplace=True) # filling 0 as a default value 
print()

df.fillna(df['Age'].mean(),inplace=True) # calculating the average value in the Age column then assign that in to the null value cells
print(f'After handling all missing values in the Age column \n\n {df.head()}')
print(df.isnull().sum())

# interpolution ==============================================================================================================================================================

data = {
    "time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}

df1 = pd.DataFrame(data)
print(f'Befor applying interpolution : \n\n {df1.head()}')
df1['value'] = df1['value'].interpolate(method='linear',inplace=True)
print()
print(f'After applying interpolution : \n\n {df1.head()}')
