import numpy as np

#----------------------------------------------- Methods for array ---------------------------------------------------

arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d.shape) # this shows the number of rows and columns ur data have
arr = np.array([[10,20,30],[40,50,60.5]])
print(arr.size) # shows the number of elements in the array
print(arr.ndim) # returns the number of dimension your array have
print(arr.dtype) # returns the data type of the array / data
integer_array = arr.astype(int)
print(integer_array.dtype)

#---------------------------------------------- Mathematical function ------------------------------------------------

mathopt = np.array([10,20,30,40,50])
print(mathopt + 5) # add 5 in each of the list element
print(mathopt * 2) # mul 2 in each element of the list
print(mathopt ** 2) # power of each element in the list

#----------------------------------------- Aggregation function -----------------------------------------------------

print(np.mean(mathopt))
print(np.min(mathopt))
print(np.max(mathopt))
print(np.std(mathopt))
print(np.var(mathopt))


