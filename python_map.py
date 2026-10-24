import streamlit as st

st.header("Python Map")

notes = """
#1 convert a list of strings to integer
s = ['1','2','3']
res = map(int, s)
print(res) # <map object at 0x107cb0840>
print(list(res)) # [1, 2, 3]

#2 map applies to each item and double the value
li = [1,2,3] 
#  #[2,4,6]
res = map(lambda x: x*2, li)
print(list(res)) # [2, 4, 6]

def double(item):
  return item*2

res = map(double, li)
print(list(res)) # [2, 4, 6]

#3 map with multiple iterables
a = [1,2,3]
b = [4,5,6]
#[5,7,9]

res = map(lambda x,y : x+y, a, b)
# print(list(res)) #[5, 7, 9]
print(tuple(res)) # (5, 7, 9)

#
fruits = [' apple ', ' banana', ' cherry']
#['APPLE', 'BANANA', 'CHERRY']
res = map(lambda item: item.strip().upper(), fruits)
print(list(res)) #['APPLE', 'BANANA', 'CHERRY']

res1 = [item.strip().upper() for item in fruits]
print(res1) #['APPLE', 'BANANA', 'CHERRY']

"""

st.code(notes, language='python')
