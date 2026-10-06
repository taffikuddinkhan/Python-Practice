
import pandas as pd # importing pandas library and giving it a early as / temporary name pd

'''

- select specific column by square bracets
- filter rows with boolean conditions

- selecting columns will return you :
                            (i) - A series with a single column
                            (ii) - A DataFrame with multiple column

- to acces single column syntax :  column = df["column name"]
- to acces multiple column syntax :  column = df[ ["column1" , "column2" , "column3" ,......] ]
- filter a row based on a single condition : df[df["column name"] > condition]
- filter  row based on multiple condition : df[ ( df["column1"] > condition1 ) & ( df["column2"] > condition2 ) ]


'''

# read data from csv file
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Data Science Roadmap Preparataion Materials\Projects\Employee.csv') # csv - comma separated file

print(df.columns)
print(df.head())

print(df["Education"]) #selected a single column
print(df[["Education","City","Age"]]) # selected multiple rows

print(df[df["Age"]>30]) # filtering a single row
print(f'Male candidates whos age are above 30 : \n\n {df[ (df["Age"]>30) & (df["Gender"] == "Male") ]}' ) # filtering multiple rows 
print()
print(f'candidates who lives in bangalore or a experience in the domain above 2 years : \n\n {df[ (df["ExperienceInCurrentDomain"]>=2) | (df["City"] == "Bangalore") ]} ') # filtering mutiple rows if any of the cndition satisfies


 