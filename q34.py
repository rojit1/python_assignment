# 34. Write a Python script to merge two Python dictionaries.

d1 = {'name': 'ram', 'age': 400}
d2 = {'a': 'apple', 'b': 'ball'}
d3 = {**d1, **d2}
print(d3)
