# 11. Write a Python program to count the occurrences of each word in a given
# sentence.


def count_occurrences(s):
    word_count = dict()

    for i in s:
        if word_count.get(i):
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count


print(count_occurrences('appleeeee'))
