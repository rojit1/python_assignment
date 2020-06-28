# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.


def find_upper_and_lower(s):
    u, l = 0, 0
    for i in s:
        if i.isupper():
            u += 1
        if i.islower():
            l += 1

    print('No. of Upper case characters : '+str(u))
    print('No. of Lower case characters : '+str(l))


find_upper_and_lower('The quick Brow Fox')
