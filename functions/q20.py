# 20. Write a Python program to find intersection of two given arrays using
# Lambda.

arr1 = [1, 2, 4, 6, 7]
arr2 = [6, 7, 9, 10]

res = list(filter(lambda x: x in arr1, arr2))
print(res)
