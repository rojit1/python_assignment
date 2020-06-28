# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.


def exchange_first_and_last(s):
    new_s = s[-1]+s[1:-1]+s[0]
    return new_s


print(exchange_first_and_last('apple'))
