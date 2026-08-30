import streamlit as st

st.header("Review Set 🍀")

notes = """
s = {10, 30, 30, 50} # {10, 50, 30}
li = [10, 20, 30]
print(s)
print(type(s)) # <class 'set'>

# convert a list to set
s = set(li)
print(s)

# methods for sets
# add item
s = {"a", "b", "c"}
s.add("d")
print(s) # {'c', 'a', 'b', 'd'}

# combine two sets into a new set
a = {1, 2}
b = {3, 4}

# way 1 to combine set
c = a.union(b)

# way 2 to combine set
c = a | b

print(c) #{ 1, 2, 3, 4}


# Intersection 
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
i = a & b # the intersection of a and b
print(i) # {2, 3}

# Difference
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
d = a - b # the set of elements in a but not b
print(d) # {1}

# Remove all elements from set
s = {1, 2, 3}
s.clear()
print(s) # set()

"""

st.code(notes, language='python')











