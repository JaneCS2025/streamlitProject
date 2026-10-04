import streamlit as st
from collections import deque

st.header("Python Deque")

# Double ended queue


notes= """
d = deque(['a', 'b', 'c'])
print(d) # deque(['a', 'b', 'c'])


#Access items in deque 
# first element of list 
# last element of the list 
print(d[0])
print(d[-1])

# # Add a element to the end of deque
d.append('d')
print(d) # deque(['a', 'b', 'c', 'd'])

# # Add a element to the beginning of the deque
d.appendleft(0)
print(d) # deque([0, 'a', 'b', 'c', 'd'])


# adds multiple elements to the right end of the deque.
d = deque([1,2,3])
l2 = [4,5,6]
# d.extend(l2)
# print(d) # deque([1, 2, 3, 4, 5, 6])

# add multiple elements to he left end of the deque
d.extendleft(l2)
print(d) #deque([6, 5, 4, 1, 2, 3])

# remove element
d = deque([10, 20, 30, 20])
d.remove(20)
print(d) # deque([10, 30, 20])
d.remove(20)
print(d) # deque([10, 30])

#pop element
d = deque([10, 20, 30, 20])
d.pop() # remove last item
print(d) # deque([10, 20, 30])

#popleft - remove 1st item
d = deque([10, 20, 30, 20])
d.popleft()
print(d) # deque([20, 30, 20])

# removes all elements from the deque
d.clear()
print(d) #deque([])

# return total number of elements from the deque
d = deque([10, 20, 30, 20])
print(len(d)) # 4

# return how many times a item appears in the deque
d = deque([1,1,1,2,2,3,3,4,5])
print(d.count(2)) #2

# rotate
d = deque([10,20,30,40])
d.rotate(2) 
print(d) #deque([30, 40, 10, 20])


d = deque([1,1,1,2,2,3,3,4,5])
d.rotate(5)
print(d) #deque([2, 3, 3, 4, 5, 1, 1, 1, 2])

# reverse
d = deque([10,20,30,40])
d.reverse()
print(d) # deque([40, 30, 20, 10])


"""

st.code(notes, language='python')