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


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) 

# [[2 3 4]
#  [7 8 9]]


