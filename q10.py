# 10. Write a Python program to remove the characters which have odd index
# values of a given string.

s = 'apple and balls'
new_s = ''
for i in range(len(s)):
    if i % 2 == 0:
        new_s += s[i]

print(new_s)
