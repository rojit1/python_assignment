# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

sample_string = 'google.com'
s = dict()
for i in sample_string:
    if not s.get(i):
        s[i] = 1
    else:
        s[i] += 1

print(s)
