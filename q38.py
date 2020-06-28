# Write a Python program to remove a key from a dictionary.


def remove_key(k, d):

    if k in d:
        del d[k]
    print(d)


remove_key('a', {'a': 10, 'b': 15, 'c': 3, 'd': 1, 'e': 2})
