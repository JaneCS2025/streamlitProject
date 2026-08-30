import streamlit as st

st.header("Review Dictionary 🍿")

notes = """
# create dictionary way1
di = {
  "name": "Jane",
  "location": "Vancouver"
}

d = dict(name="Jane", city = "Vancouver")
print(d) # {'name': 'Jane', 'city': 'Vancouver'}

# access the dictionary
#way 1
print(d['name']) 

#way 2
print(d.get('name'))

# Adding and Updating Dictionary Items
d['food'] = 'apple'
print(d)

d['name'] = 'Tina'
print(d)

# Remove Dictionary Items
d = {'name': 'Tina', 'city': 'Vancouver', 'food': 'apple'}
print(d.popitem())

# delete a key-value pair
del d['city']
print(d)

# remove all items from dictionary
d.clear()
print(d) # {}

"""

st.code(notes, language='python')

st.header("Iterating Through a Dictionary")
notes = """
st.subheader('Iterating Through a Dictionary')
d = {'a': 1, 'b': 2}

# Iterating through the keys
for key in d:
  print('key', key)

# Iterating throught the values
for value in d.values():
  print('value', value)

# Iterate key-value pair
for key, value in d.items():
  print(f'{key}: {value}')

"""
st.code(notes, language='python')

st.header("Nested Dictionary")

notes = """
d = {
  'name': 'Tina', 
  'city': 'Vancouver',
  'food': 'apple'
  }

# Nested Dictionary
d1 = {
  "student" : {
     "name": "Jane",
     "city": "Vancouver"
  }
}

print(d1['student']['name']) # Jane
print(d1['student']['city']) # Vancouver

"""
st.code(notes, language='python')

st.header("Dictionary Comprehension")

sq = {x: x**2 for x in range(1,6)}

# print(sq) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# create dictionary from two lists
keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  

d = {k:v for (k, v) in zip(keys, values)}
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

c = dict.fromkeys(range(5), 'apple')
print(c) # {0: 'apple', 1: 'apple', 2: 'apple', 3: 'apple', 4: 'apple'}



