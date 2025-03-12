'''

Given a number N return the index value of the Fibonacci sequence, where the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

For example: fibonacciRecursive(6) should return 8

'''

# Iterative Approach


def fibonacciIterative(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return 0

    fibo_array = [0, 1]

    for i in range(2, n + 1):
        fibo_array.append(fibo_array[i - 1] + fibo_array[i - 2])

    return fibo_array[n]


# print(fibonacciIterative(6))


# Recursive Approach
def fibonacciRecursive(n):
    if n < 2:
        return n

    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)
