# 30. Write a Python script to check whether a given key already exists in a
# dictionary.


def check_key_exists(k, d={}):
    if d.get(k) is not None:
        return 'Exists'
    return 'key Doesnot exists'


print(check_key_exists('c', {'a': 'apple', 'b': 'ball'}))
