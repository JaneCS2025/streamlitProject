import streamlit as st

st.header("Python Map Function")


notes = """
s = ['1','2','3','4']
res = map(int, s) # <map object at 0x109fde980>

print(list(res)) #[1, 2, 3, 4]

#double each element of the given list
li = [1, 2, 3, 4]

#1 create a function
def double(val):
  return val*2

res = map(double, li)
print(list(res)) #[2, 4, 6, 8]


#2 use lambda
res = map(lambda x: x*2, li)
print(list(res)) #[2, 4, 6, 8]

li = [1, 2, 3, 4]
# # [1,4,9,16]
res = map(lambda x: x**2, li)
print(list(res)) # [1, 4, 9, 16]

#map() with multiple iterables
a = [1,2,3]
b = [4,5,6] #[5,7,9]
res = map(lambda x, y : x+y, a, b)
print(list(res)) # [5, 7, 9]

# using map() with Tuples
nums = (1,2,3)
res = map(lambda x: x+1, nums)
print(tuple(res)) #(2, 3, 4)

#convert string to uppercase
fruits =['apple', 'banana', 'cherry']
#['APPLE', 'BANANA', 'CHERRY']
# 1st way
res = map(str.upper, fruits) 
print(list(res)) #['APPLE', 'BANANA', 'CHERRY']

# # 2nd way
res = map(lambda x: x.upper(), fruits)
print(list(res)) # ['APPLE', 'BANANA', 'CHERRY']

res = map(lambda x: x[0], fruits)
print(list(res)) # ['a', 'b', 'c']


s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res)) #['hello', 'world', 'python']

#a list of temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
# fahrenheit = (celsius * 9/5) + 32
res = map(lambda x : (x * 9/5) + 32, celsius)
print(list(res)) # [32.0, 68.0, 98.6, 212.0]

"""

st.code(notes, language='python')