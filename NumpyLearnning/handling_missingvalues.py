import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
print(arr)
print(np.isnan(arr)) # gives output in boolean value , if false then actual value if true then missing value

# Note :- you can not compare the (np.nan == np.nan) , it is not possible
print(np.nan == np.nan) # it will always return you false

cleaned_arr = np.nan_to_num(arr,nan=10) # this will replace all the missing values with the actual value which is given 10 , if not given then default value is 0
print(cleaned_arr)

infintevar_arr = np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(infintevar_arr))
cleaned_array = np.nan_to_num(infintevar_arr,posinf=50,neginf=-25) # replace the infinite values with actual value , for positive infinite value posinf and for negative infinite value neginf
print(cleaned_array)


