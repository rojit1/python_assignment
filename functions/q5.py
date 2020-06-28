# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


def find_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


print(find_factorial(5))
