# 15. Write a Python program to filter a list of integers using Lambda.
lst = [1, 3, 4, 7, 11, 34, 56]
filtered_lst = list(filter(lambda x: x < 10, lst))
print(filtered_lst)
