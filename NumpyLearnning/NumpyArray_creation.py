import numpy as np
Array =  np.array([1,2,3,4])    # 1 dimensional array
print(Array)

print()

two_dim = np.array([[1,2,3,],   # 2 dimensional array
                    [4,5,6]])
print(two_dim)

#creating array from python list
list_arr = np.array([3,4,5,6,])  # list converted into array
print(list_arr)

print()
#with default values
zero_array = np.zeros(5) # array will fill with zero
print(zero_array)

print()
# created multidimensional array of 2 row and 3 columns filled with 1s
one_array = np.ones((2,3))
print(one_array)

print()
#created multidimensional array with a particular input value
given_arr = np.full((4,4),6)
print(given_arr)

print()
#generating a sequence of numbers
sequence_gen = np.arange(1,10,2)
print(sequence_gen)

print()
#creating identity matrix
identity_matrix = np.eye(3) #identity matrix means 1 are present in diagonal side and others are 0s
print(identity_matrix)