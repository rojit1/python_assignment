# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.

sen = input('Enter a sentence : ')


def change_upper_and_lower(s):
    print(f'upper => {s.upper()} lower => {s.lower()}')


change_upper_and_lower(sen)
