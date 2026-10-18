from functools import reduce

li = ['a', 'b', 'c']

res = reduce(lambda x, y: x + " " + y, li)
print(res) # a b c


li = [1,2,3] # 6

res = reduce(lambda x, y : x + y, li)
print(res) # 6

# print(sum(li))

# Look for the largest item in the list
li = [5,8,1,3]
res = reduce(lambda maxNumber, currNumber: maxNumber if maxNumber > currNumber else currNumber, li)
print(res) #8



