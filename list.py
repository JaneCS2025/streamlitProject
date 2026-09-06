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
# create a list by squaring each number in a
a = [2, 3, 4, 5]

#[4, 9, 16, 25]
res = [ val ** 2 for val in a]
# print('res', res) # [4, 9, 16, 25]

# create a new list with only even number in a
a = [1, 2, 3, 4, 5]
res = [val for val in a if val %2 ==0 ]  # [2, 4]
# print(res)

b = [5, 12, 7, 18, 3, 20] # [3, 5, 7, 12, 18, 20]
#[12, 18, 20]

res = [val for val in b if val >= 12 ]
print(res) # [12, 18, 20]

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [i for i in range(10)]
print(res) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10)))

print([1] * 5) #[1, 1, 1, 1, 1]

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = []
# for x in mat:
#   for val in x:
#     res.append(val)

# print(res) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

res = [x for row in mat for x in row] # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(res)

"""

st.code(notes, language='python')




