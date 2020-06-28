# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def change_into_dollar(str):
    s = str[0]
    for i in range(1, len(str)):
        if str[i] == str[0]:
            s = s+'$'
        else:
            s = s+str[i]
    return(s)


print(change_into_dollar('restart'))
