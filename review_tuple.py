import streamlit as st

st.subheader("Review Tuple")

notes = """
#create tuple
a = (1,2,3)
a = tuple((1,2,3))
print(a) #(1, 2, 3)

b = tuple('Apple')
print(b) #('A', 'p', 'p', 'l', 'e')

c = tuple('Apple')
print(c[1:]) #('p', 'p', 'l', 'e')
print(c[::-1]) #('e', 'l', 'p', 'p', 'A')
print(c[:3]) # ('A', 'p', 'p')

tup = ("Geeks", "For", "Geeks")
a, b, c = tup
print(a)
print(b)
print(c)

# Concatenation of Tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)

# Deleting a tuple
tup = (0, 1, 2, 3, 4)
del tup
# print(tup) # NameError: name 'tup' is not defined.

#Unpacking with Asterisk
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) #1
print(b) #[2, 3, 4]
print(c) #5

"""

st.code(notes, language='python')