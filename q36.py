# 36. Write a Python program to sum all the items in a dictionary.

d = {'a': 10, 'b': 15, 'c': 3, 'd': 1, 'e': 2}
sum = 0
for k in d.keys():
    sum += d[k]

print(sum)
