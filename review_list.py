import streamlit as st

st.subheader("Python Tuple Review")

notes = """
tup = tuple('GEEKSFORGEEKS')
print(tup[1:]) # ('E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S')
# First way for reverse
print(tup[::-1]) # reverse string and print in a tuple ('S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G')
print(tup[4:9]) # ('S', 'F', 'O', 'R', 'G')

# Second way for reverse
t = (1, 2, 3, 4, 5) 
res = tuple(reversed(t)) 
print(res) #(5, 4, 3, 2, 1)

# Third way for reverse
tup = (3, 7, 10)  
# 3, 2, 1
for i in range(len(tup)-1, -1, -1):
  print(tup[i])

tup = tuple(t[i] for i in range(len(tup)-1, -1, -1))
print(tup) #(3, 2, 1)

# Forth way for reverse
from collections import deque
t = (1,2,3)

tup = deque(t) # in-place reversal

tup.reverse()

res = tuple(tup)

print(res) # (3, 2, 1)
"""

#code block in streamlit 
st.code(notes, language="python")

notes = """
# Set
set1={1,1,1,2,3,4,5,5,6}
print(set) # {1, 2, 3, 4, 5, 6}
print(type(set)) # <class 'set'>

# convert list to set
s = set([1,2,3])
print(s) # {1, 2, 3}

#Add a item to set
s = {"a", "b", "c"} # add 'd'
s.add("d") 
# print(s)

# Union
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
u = a | b
print(u)
print(u) # {'z', 'x', 'y'}

# Intersection
a = {1, 2, 3}
b = {2, 3, 4}
i = a & b 
i = a.intersection(b)
print(i)

# Difference
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d) #{1}

# Clear
s = {1, 2, 3}
s.clear()
print(s) #set()

"""

st.code(notes, language='python')
