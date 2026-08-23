import streamlit as st

st.subheader("Review List")

notes = """
# a = [1,2,3]
a = list((1,2,3))
print(a) # [1, 2, 3]

b = list("GFG")
print(b) # ['G', 'F', 'G']

#[2, 2, 2, 2, 2]
#[0, 0, 0, 0, 0, 0, 0] 
#Create 0 inside a list 
a = [2] * 5
b = [0] * 7
print(a)
print(b)

a = [1, 2, 2, "Python"]
print(a[0]) #1

# Add Elements to the list
# Add an element at the end of the list
a = [1,2]
a.append(3)
print(a) # [1, 2, 3]

# Add an element at a specific position
a = [1, 3]
a.insert(1, 2)
print(a) # [1, 2, 3]

# Add multiple elements to the end of the list
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a) # [1, 2, 3, 4]

# Update elements
a = [10, 20, 30, 40, 50]
a[1] = 25
# print(a) # [10, 25, 30, 40, 50]

# Remove Elements
a = [1, 2, 3]
a.remove(2)
# print(a) # [1, 3]

# Remove last element fromt the list
a = [1, 2, 3]
a.pop()
# print(a) # [1, 2]

# delete an element at specific index
a = [1, 2, 3]
del a[1]
# print(a) #[1, 3]

# clear a list
a = [1, 2, 3]
a.clear()
print(a) #[]

# Iterating over the list
a = ['apple', 'banana', 'cherry']
for item in a:
  print(item)

#Nested Lists
a = [[1,2], [3,4]]
print(a[1][0]) # 3

"""

st.code(notes, language='python')















