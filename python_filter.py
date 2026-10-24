import streamlit as st

st.header("Python Filter")

notes = """
#Filter word starts with 'a'
li = ["apple", "banana", "avocado", "cherry", "apricot"]

def starts_a(item):
  return item.startswith('a')

res = filter(starts_a, li)
print(list(res)) #['apple', 'avocado', 'apricot']

#Filter even item
a = [1, 2, 3, 4, 5, 6]
res = filter(lambda x: x%2 == 0, a)
print(list(res)) #[2, 4, 6]


#Filter item divisible by 3
a = [1, 2, 3, 4, 5, 6]
res = filter(lambda x: x%3 ==0, a)
print(list(res)) #[3, 6]

# How to remove falsey values
L = ["apple", "", None, "banana", 0, "cherry"]
res = filter(None, L)
print(list(res)) # ['apple', 'banana', 'cherry']

"""

st.code(notes, language='python')
