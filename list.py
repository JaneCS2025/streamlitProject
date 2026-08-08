import streamlit as st

st.header("Data Structures")
st.markdown("""

Data Structures are a way of storing and organizing data in a computer. \n
Algorithms is about how to solve different problems, often by searching through and manipulating data structures.\n
Understanding DSA helps you to find the best combination of Data Structures and Algorithms to create more efficient code.

Why Learn DSA with Python: \n
1.Python has a clean readable syntax \n
2.DSA allows you to improve problem-solving skills \n
3.DSA and Python helps you write more efficient code \n
4.DSA gives you a better understanding of memory storage \n
5.DSA helps you handle complex programming challenges \n
6.Python is widely used in Data Science and Machine Learning \n

""")

st.subheader("List")

notes = """
Create an algorithm to find the lowest value in a list:

my_array = [7, 12, 9, 4, 11, 8]

minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

"""

st.code(notes, language="python")

st.subheader("Time Complexity")
st.markdown("""
In the example above, the time the algorithm needs to run is proportional, or linear, to the size of the data set. This is because the algorithm must visit every array element one time to find the lowest value. The loop must run 5 times since there are 5 values in the array. And if the array had 1000 values, the loop would have to run 1000 times
""")

st.image('https://www.w3schools.com/dsa/img_runtime_findlowest.png')

st.subheader("Lists & Array Exercises")
# https://www.geeksforgeeks.org/dsa/program-to-print-multiplication-table-of-a-number/
# 1. Given a number n, check whether it is even or odd. Return true for even and false for odd.
# 2. Given a number n, we need to print its table.  
# 3. Given a positive integer n, find the sum of the first n natural numbers.
# 4. Sum of squares of first n natural numbers
# 1^2 + 2^2 + ......... + n^2 = n(n+1)(2n+1) / 6 
# 5. Swap Two Numbers
# 6. Closest to n and Divisible by m
# 7. The dice problem

Q1 = """
def isEven(n):
    # finding remainder of n
    rem = n % 2; 
    if rem == 0:
        return True
    else:
        return False

print(isEven(5))
"""
st.code(Q1, language="python")

Q2 = """
def printTable(n):

    for i in range (1, 11): 
        
        # multiples from 1 to 10
        print ("%d * %d = %d" % (n, i, n * i))

print(printTable(5))
"""
st.code(Q2, language="python")

Q3 = """
def findSum(n):
    sum = 0
    i = 1
    
    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum
"""

Q4 = """

def summation(n):
    return (n * (n + 1) * 
           (2 * n + 1)) / 6
print(summation(3))
"""

Q5 = """
# Python3 Code to swap two numbers using third variable
a = 10
b = 20

# Swap a and b using temp variable
temp = a
a = b
b = temp
print(a, b)

a = 10
b = 20

#swap two numbers using arithmetic operators
a = a + b
b = a - b
a = a - b

print(a, b)

#build in swap method
def swap(a, b):
    return b, a

a = 10
b = 20
a, b = swap(a, b)
print(a, b)

"""

Q6 = """
def closest_number(n, m):
    # find the quotient
    closest = 0
    min_difference = float('inf')

    # Check numbers around n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)

            if difference < min_difference or \
            			(difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

print(closest_number(-15, 6))

"""