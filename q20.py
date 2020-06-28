# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list = ['abc', 'xyz', 'aba', '1221']

new_list = [i for i in sample_list if i[0] == i[-1]]
print(len(new_list))
