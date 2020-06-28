# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def add_ing(st=''):
    s = ''
    if len(st) < 3:
        return st
    else:
        if st[-3:] == 'ing':
            s = st+'ly'
        else:
            s = st+'ing'
    return s


print(add_ing('string'))
