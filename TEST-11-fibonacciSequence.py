"""
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the
previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index n as
parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:
    7

the output is:
    fibonacci(7) is 13

Note: Use a for loop and DO NOT use recursion
"""


"""
# Recursion you're not supposed to use...
def fibonacci(n):
    if n < 0:
        return(-1)
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))
"""


def fibonacci(n):
    if n < 0:
        return (-1)
    else:
        fibs = [0, 1]
        for i in range(2, n + 2):
            next = fibs[i - 1] + fibs[i - 2]
            fibs.append(next)
        return (fibs[n])


if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))
