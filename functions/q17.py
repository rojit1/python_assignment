# 17. Write a Python program to find if a given string starts with a given character
# using Lambda.

a = lambda s,c: s[0] == c

if a('apple','a'):
print('yes it stats with given string')
else:
print('No')