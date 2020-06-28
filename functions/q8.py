# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.


def get_unique_list(lst):
    return list(set(lst))


print(get_unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
