# 27. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


def replace_last(lst1, lst2):
    return lst1[:-1]+lst2


print(replace_last([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
