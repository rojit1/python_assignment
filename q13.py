# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

a = input('Enter words separated by comma",": ')
x = a.split(',')
x = sorted(set([i.strip() for i in x]))
print(",".join(x))
