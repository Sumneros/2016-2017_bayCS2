from operator import sub, mul

def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))

def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    "*** YOUR CODE HERE ***"
    return Y(________)  # Replace 
