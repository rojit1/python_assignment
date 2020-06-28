# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def insert_sting_middle(s1, s2):
    middle = len(s1)//2
    return s1[:middle]+s2+s1[middle:]


print(insert_sting_middle('{{}}', 'PHP'))
