# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]


def print_even(lst):
    print([i for i in lst if i % 2 == 0])


print_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
