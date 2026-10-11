import streamlit as st

st.header("Python Lambda Functions")

notes = """
str = "learn python lambda function"
upper = lambda x: x.upper()

print(upper(str)) # LEARN PYTHON LAMBDA FUNCTION

# map function and apply a lambda expression to each element
nums = [1,2,3,4]
square = map(lambda x: x**2, nums)
print(list(square)) #[1, 4, 9, 16]

# condition checking
check = lambda x: "Positive" if x > 0 else "Negative" if x <0 else "Zero"
print(check(5)) # Positive
print(check(-3)) # Negative
print(check(0)) # Zero

# list comprehension
func = [lambda arg=x : arg*10 for x in range(1,5)]

for i in func:
  print(i())

# 10
# 20
# 30
# 40

# returning multiple results
calc = lambda x, y : (x+y, x*y)
print(calc(1,2)) #(3, 2)

# filter
c = [1,2,3,4,5,6]
even = filter(lambda x: x%2 == 0, c)
print(list(even))  #[2, 4, 6]

# reduce
from functools import reduce
a = [1,2,3]
res = reduce(lambda x, y : x+y, a)
print(res) # 6

"""

st.code(notes, language='python')
