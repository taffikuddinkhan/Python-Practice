import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_array = arr.reshape(2,3) # re shaping a single dimensional array to 2 dimension by arranging it into 2 rows 3 columns
print(reshaped_array) # the reshape don't create copy , it affects the original structure


# flattening array -----> I-ravel() - return only view , II-flatten() - return only copy , it is used to convert multidimensional array into single dimension

arr_2d = np.array([[1,2,3],[4,5,6]])

print(arr_2d.ravel())
print(arr_2d.flatten())


#inserting in single dimensional array
print("single dimensional array changes  ----------------------------------------------------")
array_mp = np.array([1,2,3,4,5,6,7,8,9])
print(array_mp)
new_arr = np.insert(array_mp,2,150)
print(new_arr)


print("multi dimensional array manupulation ----------------------------------------------------")
#inserting in multidimensional array
# inserting new row in index 1

print(arr_2d)
print()
insert2d = np.insert(arr_2d,1,[10,20],axis=1) #inserting in column wise
print(insert2d)
print()
insert2d = np.insert(arr_2d,1,[10,20,30],axis=0) # inserting row wise
print(insert2d)

# merging array through numpy
print()
arr1 = np.array([1,2])
arr2 = np.array([3,4])
arr3 = np.array([5,6])

merged_array = np.concatenate((arr1,arr2,arr3))
print(merged_array)
print()






