import streamlit as st

st.header('Python Lambda Functions')

#a lambda function to convert a string to upper case
word = 'apple'
upper = lambda x : x.upper()
print(upper(word)) # APPLE

# condition checking
# -3 # Negative
# 3  # Positive
# 0  # Zero

checkNumber = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero" 
print(checkNumber(3)) # Positive
print(checkNumber(-3)) # Negative
print(checkNumber(0))  # Zero


# List comprehension
# 10 
# 20
# 30
# 40
func = [lambda arg=x : arg*10 for x in range(1, 5)]

for i in func:
  print(i())
 
# 10
# 20
# 30
# 40

calc = lambda x, y : (x+y,  x*y)
res = calc(3, 4)
print(res) #(7, 12)

#filter()
li = [1,2,3,4,5,6]
even = filter(lambda x : x%2 ==0, li)
print(list(even)) # [2, 4, 6]

# map()
a = [1, 2, 3, 4]
double = map(lambda x: x*2, a)
print(double) # <map object at 0x10bd0c300>
print(list(double)) # [2,4,6,8]

# reduce()
from functools import reduce
a = [1, 2, 3, 4]
sumTotal = reduce(lambda x,y : x+y, a)
print(sumTotal) # 10


mul = reduce(lambda x, y: x*y, a)
print(mul) #24
