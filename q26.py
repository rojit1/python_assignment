# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.

# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


def insert_at_beginning(lst, s):
    return [s+str(i) for i in lst]


print(insert_at_beginning([1, 2, 3, 4], 'emp'))
