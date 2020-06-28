# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.


def check_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            print(f'{n} is not prime number')
            break
    else:
        print(f'{n}  is prime number')


check_prime(17)
