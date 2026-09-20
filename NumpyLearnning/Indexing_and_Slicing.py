# by indexing you only can get the exact cell value
# by using slicing you can get a list of elements
# fancy indexing can return  multiple elements by providing index value of element
# boolean indexing can return you elements by your priority or as ur need
import numpy as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])

single_array = np.array([1,2,3,4,5,6,7])

# array slicing
print(array[::-1]) # reverse element slicing

# fancy indexing
print(single_array[[2,1,0,3]]) # accessing nonsequential elements , it creates the copy of the elements not affecting the actual values

# Boolean masking technique
print(arr[arr > 3]) # print the element which are greater than 3 only