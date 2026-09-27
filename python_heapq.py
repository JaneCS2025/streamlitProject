import streamlit as st

import heapq

# Heap queue - priority queue - data structure

st.header("Python Heap Queue")

st.subheader("Heapify")


notes = """
# Convert a normal list into a heap
li = [25, 20, 15, 30, 40]
heapq.heapify(li)
print('Heap queue:', li) # Heap queue: [15, 20, 25, 30, 40]


  #       15
  #      /  \
  #    20    25
  #   /  \
  #  30  40


# Max Heap
nums = [10, 20, 15, 30, 40]
max_heap = [-n for n in nums]
print(max_heap) # [-10, -20, -15, -30, -40]

heapq.heapify(max_heap)
print(max_heap) # [-40, -30, -15, -10, -20]
print("Largest element:", -max_heap[0]) # Largest element: 40


  #       -40
  #      /  \
  #    -30  -15
  #   /  \
  # -10  -20

# appending and popping elements
li = [10, 20, 30, 15, 40]
heapq.heappush(li, 5)
print(li) # [5, 20, 10, 15, 40, 30]

#   #       5
#   #      / \
#   #    10  20
#   #   /  \  /
#   #  15  40 30

min = heapq.heappop(li)
print('remove', min) # remove 5
print(li) # [10, 20, 30, 15, 40]

min = heapq.heappushpop(li, 17)
print('remove', min) # remove 10
print(li) # [20, 15, 30, 17, 40]


# Finding largest and smaillest elements
li = [10, 20, 25, 40, 30, 70]
heapq.heapify(li)

maxi = heapq.nlargest(3, li)
print("3 Largest elements", maxi) # 3 Largest elements [70, 40, 30]

min = heapq.nsmallest(3, li)
print("3 smallest elements", min)# 3 smallest elements [10, 20, 25]

# replace and merge 
# replace - remove the smallest element and insert a new one

nums = [10, 20, 15, 30, 40]
replace = heapq.heapreplace(nums, 5)
print('replace', replace) # replace 10
print('nums', nums) # [5, 20, 15, 30, 40]


# merge function
l1 = [1, 2, 4, 3, 5]
l2 = [2, 4, 6, 8]

h = list(heapq.merge(sorted(l1), sorted(l2)))
print('sorted list', h) # [1, 2, 2, 3, 4, 4, 5, 6, 8]

"""

st.code(notes, language='python')