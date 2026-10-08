import pandas as pd # importing pandas library and giving it a early as / temporary name pd

'''
- sorting on sinle column ===================================================================================================================================================
- df.sort_values(by="column name", ascending = True - if ascending / False - if descending , inplace = True)

- sorting multiple columns ==================================================================================================================================================
- df.sort_values(by=["column1", "cplumn2"  , "column3" ] , [ ascending = True - if ascending / False - if descending ] , inplace = True)

- Aggregate functions =======================================================================================================================================================
-  summary statistics calculate like mean , median , average
- common aggregation function  : sum() , mean() , count() , min() , max() , std()

'''

# read data from csv file
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Data Science Roadmap Preparataion Materials\Projects\Employee.csv') # csv - comma separated file
print(df.head())
print()
df.sort_values(by='Age',ascending=True,inplace=True)
print(f'After sorted by age \n\n {df.head()}')
print()
print(f'Average Age {df["Age"].mean()}')
print(f'Minimum Age {df["Age"].min()}')
print(f'Maximum Age {df["Age"].max()}')

print("================================================================ Basic grouping ===================================================================================")
grouped = df.groupby("JoiningYear")['Age'].sum() # it will select a unique joining year then it will sum all of the age who are in that particular joining year
print(grouped)
