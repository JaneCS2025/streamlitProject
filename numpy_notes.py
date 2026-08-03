import streamlit as st
import numpy as np

st.header("Numpy Array Introduction")
st.markdown("""
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.

""")


arr = np.array([[1, 2, 3], [4, 5, 6]])
numpyArr = """
Create a 1-D NumPy array:

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) # class 'numpy.ndarray'
"""

st.code(numpyArr, language="python")

numpyArr = """
Create a 2-D NumPy array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
"""

st.code(numpyArr, language="python")


numpyArr = """
Create a 3-D NumPy array:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
"""

st.code(numpyArr, language="python")

# create a 5 dimensions array
arr = np.array([1,2,3,4,5], ndmin=5)


arr = np.array([1,2,3,4])
numpyArr = """
#Access Array Elements
#Get the first element from the array:

arr = np.array([1,2,3,4])
print(arr[0])

# Get third and fourth elements from the following array and add them
print(arr[2] + arr[3])
"""
st.code(numpyArr, language="python")

numpyArr = """
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1]) #2

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4]) #10

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) # output is 6

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) # 10
"""
st.code(numpyArr, language="python")

# Numpy Array Slicing
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

numpyArr = """

#Example 1
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Example 2
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

#Example 3
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) # 5, 6

#Step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

"""
st.code(numpyArr, language="python")

st.header("Numpy Data Types")

st.markdown("""
strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer \n
b - boolean \n
u - unsigned integer \n
f - float \n
c - complex float \n
m - timedelta \n
M - datetime \n
O - object \n
S - string \n
U - unicode string \n
V - fixed chunk of memory for other type ( void ) \n
""")

notes = """
arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int64

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) #u6 unicode string - the longest characters is 6

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr.dtype) #byte string, each element most 1 byte -> |S1,  "3000" → 4 bytes

"""
st.code(notes, language="python")

st.markdown("""
Converting Data Type on Existing Arrays
""")

notes = """
# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

"""

st.header("NumPy Array Copy vs View")

notes = """
# Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x) # The copy SHOULD NOT be affected by the changes made to the original array.
"""

st.code(notes, language="python")

notes = """
# Make a view, change the original array, and display both arrays:

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x) # The view SHOULD be affected by the changes made to the original array.

"""
st.code(notes, language="python")

notes =  """
Check if Array Owns its Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base attribute refers to the original object.


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy() # it owns the data, so it returns None
y = arr.view()

print(x.base) # The copy returns None.
print(y.base) # The view returns the original array.
"""

# Mean, Median, and Mode
st.header("Mean, Median, and Mode")
st.markdown("""
In Machine Learning (and in mathematics) there are often three values that interests us:

Mean - The average value
Median - The mid point value
Mode - The most common value

""")

# Get Mean
notes = """
# Use the NumPy mean() method to find the average speed:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)

print(x)

"""

# Get Median 
# The median value is the value in the middle, after you have sorted all the values:
# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
# 87 is the median

notes = """
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

"""

# Get Mode
# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

notes = """
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

"""
