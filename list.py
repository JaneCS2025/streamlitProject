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
