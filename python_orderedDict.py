import streamlit as st

from collections import OrderedDict

notes =  """
od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

print(list(od.items())) # [('apple', 1), ('banana', 2), ('cherry', 3)]

# regular dictionary
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d']= 4

for key, value in d.items():
  print(key, value)

# a 1
# b 2
# c 3
# d 4

od = OrderedDict()
od['c'] = 3
od['a'] = 1
od['b'] = 2
od ['d'] =4

for key, value in od.items():
  print(key, value)

# c 3
# a 1
# b 2
# d 4

# change 'c' to 5 
od = OrderedDict([('c', 3), ('a', 1), ('b', 2), ('d', 4)])
od['c'] = 5
for key, value in od.items():
  print(key, value)

# c 5
# a 1
# b 2
# d 4


# Equality checks consider order

od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('b', 2), ('c', 3), ('a', 1)])

print(od1 == od2) # False


d1 = {'a': 1, 'b':2, 'c': 3}
d2 = { 'b':2, 'c': 3, 'a': 1}
print(d1 == d2 ) # True

#Reverse an Ordered Dict
[('a', 1), ('b', 2), ('c', 3)]

d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d2 = OrderedDict(reversed(d1.items()))

for key, value in d2.items():
  print(key, value)

# c 3
# b 2
# a 1

#Remove the last item from Ordered Dict
d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# res = d1.popitem() 
# print(res) # ('c', 3)

#Remove a specific item  
d1.pop('b')
print(d1) # OrderedDict({'a': 1, 'c': 3})

d1['b'] = 2
# print(d1) # OrderedDict({'a': 1, 'c': 3, 'b': 2})

for key, value in d1.items():
  print(key, value)

# a 1
# c 3
# b 2

# Move keys to the end
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d.move_to_end('a')
print(d) # OrderedDict({'b': 2, 'c': 3, 'a': 1})

# for key, value in d.items():
#   print(key, value)

# b 2
# c 3
# a 1

# Move keys to the front
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d.move_to_end('c', last = False)
print(d) # OrderedDict({'c': 3, 'a': 1, 'b': 2})

"""

st.code(notes, language='python')
