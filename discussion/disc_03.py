from typing import Counter


def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return multiply(m, n-1) + m
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    else:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        
        return hailstone(n) + 1

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(y):
        if y == 0:
            return x
        else:
            
            return f(repeat(y - 1))
    return repeat
    
def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
"""Implement the recursive is prime function. Do not use a while loop, use
recursion. As a reminder, an integer is considered prime if it has exactly two
unique factors: 1 and itself."""
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
def prime_helper(n, i=2):
    if n % 2 == 0 or n == 1:
        return False
    elif i == n:
        return True
    else:
        if n % i == 0:
            return False
        else:
            i += 1
            return prime_helper(n, i)
    

        
