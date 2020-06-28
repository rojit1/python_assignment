# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


print(sum_list([8, 2, 3, 0, 7]))
