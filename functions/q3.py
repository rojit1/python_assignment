# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def multiply_elements(lst):
    ans = 1
    for i in lst:
        ans *= i
    return ans


print(multiply_elements([8, 2, 3, -1, 7]))
