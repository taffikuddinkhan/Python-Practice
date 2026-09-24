# without using for loop performing a single operation on all the elements is known as broadcasting
import numpy as np

price = np.array([100,200,300])
discount = 10
final_price = price - (price * discount/100 )  # substraction 10% from each of the elements
print(final_price)

print(price * 2) # we don't need to iterate through each element and perform the same operation , instead of that numpy provides broadcasting

print()
matrix = np.array([[1,2,3],[4,5,6]])
array = np.array([10,20,30])

print(matrix + array)  # broadcasting , added array elements throughout each of the matrix element
print(matrix * array)
print(matrix - array)
