import pandas as pd # importing pandas library and giving it a early as / temporary name pd

# read data from csv file
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Data Science Roadmap Preparataion Materials\Projects\Employee.csv') # csv - comma separated file

# if u getting any encoding error that means the text are not understand by ur system , so ui have to pass it manually , there are 2 types of encoding="utf-8" , encoding="latin1"
# print(df)

# converting a dictionary to a csv file
data = {
    "name":['kokushibo','akaza','doma'],
    "age":[1400,400,350],
    "city":['bbsr','ctck','khordha']
}

df1 = pd.DataFrame(data) # converting the dictionary in to an dataframe
# print(df1)

df.to_csv("output.csv",index=False)  # it will create an csv file named output for you 
df.to_excel("output.xlsx",index=False)  # it will create an excel file named output for you
df.to_json("output.json",index=False)  # it will create an json file named output for you

print("display first 5 rows : ---------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.head(10)) # display first 10 rows 

print("display last 5 rows : ----------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.tail(10)) # printing last 10 rows

print("Displaying the information of the dataset --------------------------------------------------------------------------------------------------------------------------------")
print(df.info()) # give a brief information about your dataset , like datatypes , number of rows and columns , missing/null values 
# The rangeindex shows the present / current rows availavle in the dataset
# Data columns tells the number of columns in your dataset 

print("Describing the dataset ----------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.describe())  # describing statistical values by analysing the dataset such as min , max , average , std , 25% , 50% , 75%

print("Number of rows and columns in the dataset ---------------------------------------------------------------------------------------------------------------------------------")
print(df.shape) # shows the number of rows and columns you have in your dataset

print("The name of individual columns present in the dataset ----------------------------------------------------------------------------------------------------------------------")
print(df.columns) # shows each column name so that you can access each individual column according to your needs 

