import streamlit as st
from functools import reduce


notes = """
#1 Add up all the strings in the list
li = ['a', 'b', 'c']

r = reduce(lambda x, y : x+' '+y, li)
print(r) #a b c
 

#2 Sum the values in a list
a = [2, 4, 6, 8]
res = reduce(lambda x,y : x+y, a)
print(res) #20


#3 Find the largest value in the list
a = [5, 9, 3, 12, 7]

res = reduce(lambda x, y : x if x > y else y, a)
print(res) # 12

"""

st.code(notes, language='python')



