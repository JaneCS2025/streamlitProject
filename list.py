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
# Square each number in the list
a=[2,3,4,5]
#way1
output = list(map(lambda x: x ** 2, a))
#way2
res = [val ** 2 for val in a]
#output
# [4, 9, 16, 25]

# New list return only even numbers
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
#output
# [2, 4]

# New list return result based on condition
a = [5, 12, 7, 18, 3, 20] # [3, 5, 7, 12, 18, 20]
res = [val for val in a if val >10]
res = [a[i] for i in range(len(a)) if i % 2 ==1]
#output:
# [12, 18, 20]
print(res)

# Create a list from a range
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [i for i in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([1]*5) # [1, 1, 1, 1, 1]

# Flatten the list 
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # [ val1, val2, val3] -> val1 = [1, 2, 3]
#output 
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

res = [val for item in a for val in item]
print(res)

"""

st.code(notes, language='python')






