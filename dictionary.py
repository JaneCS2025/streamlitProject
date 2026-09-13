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

notes = """

dict = {}
# Way 1
for k in range(1,6):
  dict[k]= k**2 # key, value pair in dict

# print(dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Way 2
dict = {k: k**2 for k in range(1,6)}
print(dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Creating a Dictionary from Two Lists
keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]


# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# Way 1
dict = {}

for i in range(len(keys)):
  dict[keys[i]] = values[i]

print(dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Way 2

dict1 = {k:v for (k,v) in zip(keys, values)}
print(dict1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# {0: True, 1: True, 2: True, 3: True, 4: True}

#Way 1
dict = {}

for i in range(5):
  dict[i] = True

print(dict) # {0: True, 1: True, 2: True, 3: True, 4: True}

# Way 2
dict1 = dict.fromkeys(range(5), True)
print(dict1) # {0: True, 1: True, 2: True, 3: True, 4: True}


#{'apple': 5, 'banana': 6, 'cherry': 6}
# way 1
keys = ['apple', 'banana', 'cherry']
dict = {}

for key in keys:
  dict[key] = len(key)

print(dict) # {'apple': 5, 'banana': 6, 'cherry': 6}

# way 2
dict = {key: len(key) for key in keys}

print(dict) #{'apple': 5, 'banana': 6, 'cherry': 6}

# way 1
dict = {}

for i in range(9):
  if i % 2 == 0:
    dict[i] = i**3

print(dict) # {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}


# way 2
dict = {key : key**3 for key in range(9) if key % 2 == 0}
print(dict) # {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

"""

st.code(notes, language='python')



