import streamlit as st
import numpy as np

st.header("Numpy Array Introduction")
st.markdown("""
NumPy is a Python library used for working with arrays. \n
It also has functions for working in domain of linear algebra, fourier transform, and matrices. 
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely. 
NumPy stands for Numerical Python.
""")

# arr = np.array([1,2,3,4,5])
# st.write(arr)

numpy_1_dimension = """
#Create a 1-D Numpy array
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
"""

#create code block
st.code(numpy_1_dimension, language='python')


numpy_2_dimension = """
# 2 Dimension array
arr= np.array([[1,2,3], [4,5,6]])
print(arr)

"""
st.code(numpy_2_dimension, language='python')


numpy_3_dimension = """
# 3 Dimension array
arr = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(arr)
"""
st.code(numpy_3_dimension, language='python')


notes = """
#Access Array Elements
arr = np.array([1,2,3])
print(arr[0])

print(arr[1] + arr[2])

#Access 2D array to get value
arr = np.array([[1,2,3],[4,5,6]])
print(arr[1, 0]) #4

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]]) # print 10
print(arr[1,4]) 

#How to access 3D array value
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])  # 6

# Print last element of the 2D array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, -1]) #10 
"""
st.code(notes, language="python")


#Numpy Array Slicing 
st.header("Numpy Array Slicing")
st.markdown("""
Slicing arrays
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1

""")



notes = """
Example of slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[0:5:1]) # equal print(arr[:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3: -1]) # [5 6]

# Step Example
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) #[2 4]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) #[1 3 5 7]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) 
print(arr[1, 1:3]) # [7 8]

#From both elements, return index 2
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) #[3 8]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) 

#output
# [[2 3 4]
#  [7 8 9]]

"""

st.code(notes, language='python')

st.subheader("Converting Data Type on Existing Arrays")

notes = """
Below is some examples:

arr = np.array([12,23,34,45,55], dtype='S')
print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

#convert float to integer
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr) # [1 2 3]
print(newarr.dtype) #int32

#convert integer to boolean
arr = np.array([-1, 0, -3])
newarr = arr.astype(bool) 
print(newarr) #[ True False  True]
print(newarr.dtype) #bool

"""

st.code(notes, language= 'python')

st.subheader("The Difference Between Copy and View")

notes = """
arr = np.array([1,2,3])
arr2 = arr.copy() # The copy SHOULD NOT be affected by the changes made to the original array.
arr[0] = 42

print(arr)
print(arr2) 


arr3 = arr.view()
arr[0] = 42
print(arr) # The view SHOULD be affected by the changes made to the original array.
print(arr3) 

arr3 = arr.view()
arr3[0] = 10

print(arr)
print(arr3)

# Check if Array owns its original data 
arr = np.array([1,2,3])
arr1 = arr.copy()
arr2 = arr.view()

print(arr1.base) # None
print(arr2.base) # Original array


# Example for copy and view
original_array = np.array([1, 2, 3])
x = original_array.copy()
x[0] = 5
print(original_array)
"""

st.code(notes, language='python')

st.subheader("Get the Shape of an Array")

notes = """
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #(2, 4)

Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1,2,3,4], ndmin=5)
print(arr) # [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape)  # (1, 1, 1, 1, 4)

arr = np.array([[1, 2], [5, 6], [7, 8]])
print('shape of array :', arr.shape) # (3, 2)

"""
st.code(notes, language='python')


st.subheader('Reshaping arrays')

notes = """
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# row * columns  = total elements in the list 
newArr = arr.reshape(4, 3) 
print(newArr)

newArr = arr.reshape(3, 4)
print(newArr)

newArr = arr.reshape(2, 6)
print(newArr)


# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# 1D array with 12 elements into a 3D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # 12

newArr = arr.reshape(2,3,2) 
print(newArr)

# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

# Pass -1 as the value, and Numpy will calculate this number for you
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newArr = arr.reshape(2,2,-1)
print(newArr)

# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

# Flattening the arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
newArr = arr.reshape(-1)

print(newArr) #[1 2 3 4 5 6]
"""

st.code(notes, language='python')

st.subheader("Iterating Arrays")

notes = """

# 1D array
arr = np.array([1, 2, 3])

for x in arr:
  print(x) # 1,2,3


#2D array
1 2 3 4 5 6
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr: #[1, 2, 3], [4, 5, 6]
  for y in x: 
    print(y)

for x in arr:
  for y in x:
    for z in y:
      print(z)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(arr):
  print(x)

#skip number using step
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

"""

st.code(notes, language='python')

st.subheader("Joining NumPy Arrays")

notes = """
# example 1
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
# print(arr) #[1 2 3 4 5 6]

#example 2
# Join two 2-D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)
# [[1 2 5 6]
# [3 4 7 8]]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)

# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# using stack to join array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# [[1 4]
#  [2 5]
#  [3 6]]

# Stacking Along Rows using hstack
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print(arr) #[1 2 3 4 5 6]


#Stacking Along Columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
# print(arr)
# [[1 2 3]
#  [4 5 6]]

# Stacking Along Height (depth)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))

print(arr)
# [[[1 4]
#   [2 5]
#   [3 6]]]

"""

st.code(notes, language='python')

st.subheader("NumPy Splitting Array")

notes = """

# Split one dimension array
arr = np.array([1,2,3,4,5,6])
newArr = np.array_split(arr, 3)

print(newArr)
print(newArr[0])
print(newArr[1])
print(newArr[2])

# Splitting 2-D Arrays

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newArr = np.array_split(arr, 3)
print(newArr)
print(newArr[0])
# [[1 2]
#  [3 4]]


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArr = np.array_split(arr, 3)
print(newArr)
print(newArr[0])
# [[1 2 3]
#  [4 5 6]]


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArr = np.array_split(arr, 3, axis=1)
print(newArr)


#hsplit - opposite of hstack
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArr = np.hsplit(arr, 3)
print(newArr)

#vsplit
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArr = np.vsplit(arr, 3)
print(newArr)


#dsplit - work on 3 or more dimensions - split by depth
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])
newArr = np.dsplit(arr, 3)
print(newArr)
"""

st.code(notes, language='python')

st.subheader("Searching Arrays")

notes = """
arr = np.array([1, 2, 3, 4, 5, 4, 4])

res = np.where(arr == 4)
# print(res) # array([3, 5, 6])

# checking the odd number
arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr%2 == 1) 
# print(x) #(array([2, 3, 5]),)

arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr%2 == 0) 
# print(x) # (array([0, 1, 4]),)


# Find the index to insert a number in a sorted array
arr = np.array([6, 7, 8, 9])
res = np.searchsorted(arr, 7)
# print(res) # index 1 is the location to insert 7

#insert 7 from the end
arr = np.array([6, 7, 8, 9])
res = np.searchsorted(arr, 7, side="right")
# print(res) # 2

#insert multiple values
arr = np.array([6, 7, 8, 9])
res = np.searchsorted(arr, [2, 4, 6])
# print(res) # [0, 0, 0]

arr = np.array([1, 3, 5, 7])
res = np.searchsorted(arr, [2, 4, 6])
print(res) # [1 2 3]

"""

st.code(notes, language='python')

st.subheader("Sorting a 2D Array")

notes = """
arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))
# [[2 3 4]
#  [0 1 5]]

arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr)) # ['apple' 'banana' 'cherry']

arr = np.array([True, False, True])
print(np.sort(arr)) # [False  True  True]
"""

st.code(notes, language='python')

st.subheader("Creating Filter Directly From Array")

notes = """
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42

newArr = arr[filter_arr]
# print(filter_arr) #[False False  True  True]
# print(newArr) # [43 44]

arr = np.array([41, 42, 43, 44])
mask = [True, False, True, False]

newArr = arr[mask] 
# print(newArr) #[41 43]

# return only even numbers from original array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for ele in arr:
  if ele %2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newArr = arr[filter_arr]
# print(filter_arr) # [False, True, False, True, False, True, False]
# print(newArr) # [2 4 6]

#way2 to filter even number
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr %2 == 0

newArr = arr[filter_arr]
print(newArr) # [2 4 6]

"""

st.code(notes, language='python')

