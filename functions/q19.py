# 19. Write a Python program to create Fibonacci series upto n using Lambda.


def fib(n):
    fib = [0, 1]

    any(map(lambda _: fib.append(sum(fib[-2:])),
            range(2, n)))

    return fib[:n]


print(fib(5))
