# Write a Python function to check whether a number is in a given range.


def check_range(num, low, high):
    return num < high and num >= low


print(check_range(10, 5, 20))
