#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given non-negative integer
    using recursion. The factorial of a number n is the product of all
    positive integers from 1 to n.

    Parameters:
    n (int): A non-negative integer whose factorial will be calculated.

    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)