def repeat(k):
    """When called repeated, print each repeated argument.

    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)

def detector(f):
    def g(i):
        if f(i):
            print(i)
        return detector(lambda j: j == i)
    return g
repeat(1)(7)(3)(4)(2)(5)(1)(6)(5)(1)