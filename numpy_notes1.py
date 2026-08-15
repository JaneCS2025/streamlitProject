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












