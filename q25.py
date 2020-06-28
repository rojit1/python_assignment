# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.

# Sample list : [{},{},{}]
# Return value : True

# Sample list : [{1,2},{},{}]
# Return value : False


def check_empty(ls):
    for i in ls:
        if bool(i):
            return False
    return True


print(check_empty([{}, {}, {}]))
