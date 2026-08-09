import streamlit as st

st.header("Data Structures")

st.markdown("""
Data Structures are a way of storing and organizing data in a computer.

Algorithms is about how to solve different problems, often by searching through and manipulating data structures.

Understanding DSA helps you to find the best combination of Data Structures and Algorithms to create more efficient code.

Why Learn DSA with Python:

1.Python has a clean readable syntax

2.DSA allows you to improve problem-solving skills

3.DSA and Python helps you write more efficient code

4.DSA gives you a better understanding of memory storage

5.DSA helps you handle complex programming challenges

6.Python is widely used in Data Science and Machine Learning

""")

notes = """
#Q1: Create an algorithm to find the lowest value in a list
my_array = [7, 12, 9, 4, 11, 8] #4

def findLowestValue(list):
  lowestValue = my_array[0]

  for i in list:
    if i < lowestValue:
      lowestValue = i

  return lowestValue

print(findLowestValue(my_array))
"""

st.code(notes, language = 'python')

# Time complexity

st.header("Time Complexity")

st.markdown("""
In the example above, the time the algorithm needs to run is proportional, or linear, to the size of the data set. 
This is because the algorithm must visit every array element one time to find the lowest value. 
The loop must run 5 times since there are 5 values in the array. 
And if the array had 1000 values, the loop would have to run 1000 times

""")

st.image("https://www.w3schools.com/dsa/img_runtime_findlowest.png")

q2_notes = """

# Q2: Given a number n, check whether it is even or odd. Return true for even and false for odd.
def isEven(num):
  rem = num %2
  if rem == 0:
    return True
  else:
    return False

print(isEven(11))

"""
st.code(q2_notes, language='python')


q3_notes = """
  
  Q3: Given a number n, we need to print its table like below format.

  For example:
  5 * 1 = 5
  5 * 2 = 10
  5 * 3 = 15
  5 * 4 = 20
  5 * 5 = 25
  5 * 6 = 30
  5 * 7 = 35
  5 * 8 = 40
  5 * 9 = 45
  5 * 10 = 50

  def printTable(n):

    for i in range(1,11):
      print("%d * %d = %d" % (n, i, n * i))

  print(printTable(5))
  print(printTable(7))

"""

st.code(q3_notes, language='python')


#Q4
#Given a list like below and please return the sum of the list
my_array = [7, 12, 9, 4, 11, 8]


#Q5 Swap Two Numbers
num1 = 2
num2 = 3

#output 
num1 = 3
num2 = 2

#Q6 The dice problem
dice = 2 # opposite of number   d=1 -> oppo=6, d=2 , oppo=5, d =3, oppo = 3