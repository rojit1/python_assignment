# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.


def return_longest(lst):
    return max(len(el) for el in lst)


print(return_longest(['apple', 'ball', 'cat']))
