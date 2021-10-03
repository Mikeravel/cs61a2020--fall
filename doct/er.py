def search(f):
    x = 0
    while not f(x):
        x += 1
    return x
def is_three(x):
    return x == 3
def square(x):
    return x * x
def positive(x):
    return max(0, square(x) - 100)
def inverse(f):
    """Return  a function g(y)  that returns x such that f(x) == y
    >>> sqrt = inverse(square)
    >>> sqrt(16)
    4"""
    def is_inverse_of_f(x):
        return f(x) == y
    return search (is_inverse_of_y)
return inverse_of_f
#return lambda y: search(lambda x : f(x) == y)
    