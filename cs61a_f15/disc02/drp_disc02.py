# 2015 Discussion 2 Recursion! Recursion! (Tree) Recursion!
# implemented by drP

# 1.1 Cool Questions
# 1.1.1
def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    print(n)
    if n == 1:
        return
    return countdown(n - 1)
    
# 1.1.2
# Is there an easy way to change COUNTDOWN to count up instead?
def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """
    if i == n:
        print(n)
        return
    return countup(i + 1)
    
    
# 1.1.3
# Write a procedure expt(base, power), which implements the exponent
# function. Assume power is always an integer. Use recursion, not pow!

def expt(base, power):
    """
    >>> expt(3, 2)
    9
    >>> expt(2, 3)
    8
    """
    if power == 1:
        return base
    else:
        return base * expt(base, power - 1)

# 1.1.4
# Fill in the IS_PRIME function, which returns True if n is a prime number
# and False otherwise. Hint: We wrote this iteratively last week, but this
# time use recursion!

def is_prime(n):
    """
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
# YOUR CODE HERE #

# 1.1.5
# Write SUM_PRIMES_UP_TO(n), which sums up every prime up to and including n.
# Assume you have an IS_PRIME() predicate.

def sum_primes_up_to(n):
    """
    >>> sum_primes_up_to(10)
    15
    """
# YOUR CODE HERE #

# 1.1.6
# Draw an environment diagram for the following code:
def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
rec(3, 2)

# Bonus question: what does this function do?
    
# 2.1 Exercises
# 2.1.1 I want to go up a flight of stairs that has n steps. I can either
# take 1 or 2 steps each time. How many different ways can I go up this
# flight of stairs? Write a function COUNT_STAIR_WAYS that solves this problem.

def count_stair_ways(n):
    """
    >>> count_stair_ways(6)
    13
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


# I think that's enough for now - drP