# Keep it Simple, Stupid (KISS)


# Wrong way
def factorial(n):
    result = 1
    if n < 0:
        return "Factorial of negative number doesn't exist"
    elif n == 0:
        return 1
    else:
        for i in range(2, n + 1):
            result *= i
    return result


# Right way
import math


def factorial(n):
    if n < 0:
        return "Factorial of negative number doesn't exist"
    else:
        return math.factorial(n)
