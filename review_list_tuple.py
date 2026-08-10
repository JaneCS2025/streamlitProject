# 8/15/2026 review python list function
# Data Structures - https://www.geeksforgeeks.org/python/python-programming-language-tutorial/

# Create a list and print it 
b = ["apple", "banana"]
print(b)

# Using list() Constructor:
# What will print out for below? 
a = list((1, 2, 3, 'apple', 4.5))  
print(a) # [1, 2, 3, 'apple', 4.5]

b = list("GFG")
print(b) # ['G', 'F', 'G']

# Creating List with Repeated Element
a = [2] * 5
b = [0] * 7

print(a) # [2, 2, 2, 2, 2]
print(b) # [0, 0, 0, 0, 0, 0, 0]

# Access Elements
# Get access to the last element of the list 
a = [10, 20, 30]
print(a[-1])

# Nested Lists
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0]) # 3

# Tuple
# Convert list to a tuple ?
li = [1, 2, 4, 5, 6]
print(tuple(li))

# What will be the output for below
tup = tuple('Geeks')
print(tup) # ('G', 'e', 'e', 'k', 's')

# How to concatenate two tuples together ?
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)

tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

#Tuple Unpacking with Asterisk (*)
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)

#Reversing a Tuple
#way1 
t = (1, 2, 3, 4, 5) 
rev = t[::-1]
print(rev)

#way2
t = (1, 2, 3, 4, 5) 
rev = tuple(reversed(t))
print(rev)

#way3 - using a loop
#reverse the tuple by iterating through the indices in reverse order
t = (1, 2, 3, 4, 5) 
rev = tuple(t[i] for i in range(len(t)-1, -1, -1))
print(rev)

#way4 - using collecting.deque
from collections import deque
t = (1, 2, 3, 4, 5) 
deq = deque(t)
deq.reverse()

rev = tuple(deq)
print(rev)

# String 
#remove empty space from a string 
s = "   ABC   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome")) # replace fun to awesome

# string comparison
s1 = "apple"
s2 = "banana"

print(s1 == s2) 
print(s1 != s2)
print(s1 < s2)

# What will be the output for above
# print(s1 == s2)  # False
# print(s1 != s2)  # True
# print(s1 < s2) # True

# Convert Integer to String in Python
# way 1
n = 42
s = str(n)

print(s)
print(type(s))

# using f string
# way 2 
n = 42
s = f"{n}"

print(s)
print(type(s))

# using format() function
# way 3
n = 42
s = "{}".format(n)

print(s)
print(type(s))

# Using %s Formatting
# way 4
n = 42
s = "%s" % n

print(s)
print(type(s))

# Convert string into int in python
# int() Function
s = "42"
num = int(s)
print(num)
print(type(num))

# Converting Strings with Different Bases
# Binary string
s = "1010"
num = int(s, 2) # 10
print(num)

# Hexadecimal string
s = "A"
num = int(s, 16) # 10
print(num)

# Handling Invalid Input String
# How to handle error in python ???
s = "abc"
try:
    num = int(s)
    print(num)
except ValueError:
    print("Invalid input: cannot convert to integer")

#str.isdigit()
s = "12345" # s = "abc"
if s.isdigit():
    num = int(s)
    print(num)
else:
    print("The string is not numeric.")

# Convert String to a list in python
# Using split()
s = "Python programming language"
a = s.split()
print(a)

# Using list()
s = "Python"
a = list(s)
print(a)

# Using List Comprehension
s = "Python"
a = [ch for ch in s]
print(a)

s = "Python,Java,C++"
a = s.split(",")
print(a) # ['Python', 'Java', 'C++']

# Multi-dimensional Lists in Python
# A multidimensional list is created by nesting lists within a single list. It allows data to be organized in rows and columns, similar to a matrix or table.
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

m, n = 4, 5
mat = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)

print(mat)

# Accessing a Multidimensional List
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
for row in a:
    print(row)

# output: 
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
 
# Using Index-Based Nested Loops
# a = [[2, 4, 6, 8], 
#      [1, 3, 5, 7], 
#      [8, 6, 4, 2], 
#      [7, 5, 3, 1]] 
        
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
#     print()

# 2 4 6 8 
# 1 3 5 7 
# 8 6 4 2 
# 7 5 3 1 

# Methods on Multidimensional Lists
# using append
# Link: https://www.geeksforgeeks.org/python/multi-dimensional-lists-in-python/

a = [[2,4,6],[3,6,9]]
a.append([5,10,15])
print(a)

#[[2, 4, 6], [3, 6, 9], [5, 10, 15]]

# Using extend()
a = [[2,4,6],[3,6,9]]
a[0].extend([8,10])
print(a)

#[[2, 4, 6, 8, 10], [3, 6, 9]]

# Using reverse()
a = [[2,4,6],[3,6,9]]

a[1].reverse()   # reverse second row
print(a)         # [[2, 4, 6], [9, 6, 3]]
a.reverse()      # reverse row order
print(a)         # [[9, 6, 3], [2, 4, 6]]


# Using Indexing to Read/Write Element
a = [[1,2],[3,4]]

print(a[0][1])   # read
a[1][0] = 9      # write
print(a)

# Using List Comprehension for Processing Rows
a = [[1, 2, 3], [4, 5, 6]]
b = [[ x*2 for x in row ] for row in a] 
print(b)

# [[2, 4, 6], [8, 10, 12]] - output








