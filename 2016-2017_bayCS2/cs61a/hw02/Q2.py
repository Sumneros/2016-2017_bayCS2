from operator import add, mul

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1


def accumulate(combiner, base, n, term):
    """Return the result of combining the first N terms in a sequence.  
    The terms to be combined are TERM(1), TERM(2), ..., TERM(N).  COMBINER 
    is a two-argument function.  Treating COMBINER as if it were a binary 
    operator, the return value is BASE COMBINER TERM(1) COMBINER TERM(2) ... COMBINER TERM(N)

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"
def summation_using_accumulate(n, term):
    """Returns the sum of TERM(1) + ... + TERM(N). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return _______

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return _______
