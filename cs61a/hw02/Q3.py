def true(x):
    return True

def false(x):
    return False

def odd(x):
    return x % 2 == 1

def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate PRED.  COMBINER is a two-argument function.
    If v1, v2, ..., vk are the values in TERM(1), TERM(2), ..., TERM(N)
    that satisfy PRED, then the result is
         BASE COMBINER v1 COMBINER v2 ... COMBINER vk
    (treating COMBINER as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, true, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, false, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, odd, 5, square)  # 1 * 1 * 9 * 25
    225
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion', 'FunctionDef'])
    True
    """
    "*** YOUR CODE HERE ***"
    return _______
