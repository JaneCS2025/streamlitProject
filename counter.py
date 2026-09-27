from collections import Counter
import streamlit as st

st.header('Python Collections Counter')

notes = """
#example of Counter

list = [1,1,1,2,2,2,3,4]

res = Counter(list)

print(res) #Counter({1: 3, 2: 3, 3: 1, 4: 1})

# string example for counter
str = "Hello World"
res = Counter(str)
# print(res) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})


tup = (1,1,2,2,4,4)
res = Counter(tup)
print(res) # Counter({1: 2, 2: 2, 4: 2})

#Accessing Counter Elements
ctr = Counter([1,1,1,2,2,3,3,3]) # Counter({1: 3, 3: 3, 2: 2})

print(ctr[1]) #3 
print(ctr[2]) #2
print(ctr[3]) #3
print(ctr[10]) #0


#Counter Methods
#1. update
ctr = Counter([1,1,2])
ctr.update([8,9,10])

# print(ctr) # Counter({1: 2, 2: 1, 8: 1, 9: 1, 10: 1})

#2. element() -> return a list
ctr =  Counter([1,1,2])
res = list(ctr.elements()) # [1, 1, 2]
# print(res)


#3 most_common()
ctr = Counter([1,2,2,2,3,3])
common = ctr.most_common(2) # most common, 2nd most common, 3rd most common....
print(common)  # [(2, 3), (3, 2)]

"""

#Counter Operations
# ctr1 = Counter([1, 2, 2, 3])
# ctr2 = Counter([2, 3, 3, 4])

# print(ctr1 + ctr2) # Addition # Counter({2: 3, 3: 3, 1: 1, 4: 1})
# print(ctr1 - ctr2) # Subtraction Counter({1: 1, 2: 1})
# print(ctr1 & ctr2) # Intersection Counter({2: 1, 3: 1})
# print(ctr1 | ctr2) # Union Counter({2: 2, 3: 2, 1: 1, 4: 1})




st.code(notes, language='python')

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
#Use Python’s Counter to find:
#How many of each fruit are in the bag and which fruit appears the most

counts = Counter(fruits)

print(counts) # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counts.most_common(1)[0]) # ('apple', 3)




