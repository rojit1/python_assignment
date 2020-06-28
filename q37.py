# 37. Write a Python program to multiply all the items in a dictionary.

d = {'a': 10, 'b': 15, 'c': 3, 'd': 1, 'e': 2}
sum = 1
for k in d.keys():
    sum *= d[k]

print(sum)
