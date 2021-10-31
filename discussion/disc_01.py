def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining == True:
        return True
    else:
        return False
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n % 2 == 0 or n == 1:
        return False
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return True
    

