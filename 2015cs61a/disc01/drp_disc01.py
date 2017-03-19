from operator import add, mul, sub, mod, truediv, floordiv, lt, gt, eq, le, ge

# 1.3 Questions

# Question 1. Alfanso will only wear a jacket it the temperature is below
# 60 degree or if it raining.  This should take only one line of code:

def wears_jacket(temp, raining):
    """
    >>> rain = False
    >>> wears_jacket(90, rain)
    False
    >>> wears_jacket(40, rain)
    True
    >>> wears_jacket(100, True)
    True
    """
##### Your code here #####  


# Question 2. To handle discussion section overflow ...
# NB: The Solution provided on the cs61a schedule is not correct
# because it will print "1 spots ..."

def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow
    >>> handle_overflow(35, 29)
    1 spot in Section 2.
    >>> handle_overflow(20, 32)
    10 spots left in Section 1.
    >>> handle_overflow(35, 30)
    No space left in either section
    """
##### Your code here  #####    


# 1.5 Questions

# Question 1: What is the resukt of evaluating the followiing code?
# def square(x):
#   return mul(x, x)
# def so_slow(num):
#   x = num
#   while x > 0:
#       x = add(1, x)
#   return x/0
# square(so_slow)
#
# Ans: an infinite loop

# Question 2: Fill in the is_prime function to return True iff argument
# is prime.

def is_prime(n):
    """
    >>> is_prime(1)
    False
    >>> is_prime(0)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(8)
    False
    >>> is_prime(11)
    True

    """
##### Your code here ########

# 1.6 Have Some More Control
# Question 1: Implement fizzbuzz:
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None
    True
    """
##### Your code here #####

# Question 2: Fill in the choose function (ways to choose k from n)

def choose(n, k):
    """Returns the number of ways to choose K items from
        N items.
        
    >>> choose(5,2)
    10
    
    >>> choose(20,6)
    38760
    """
##### Your code here #####

# 2.2 Questions
# Question 1 requires no coding
# Question 2: Implement keep_ints

def keep_ints(cond, n):
    """Prints out all integers 1 ..i..n where cond(i) is True.
    
    >>> def is_even(x): return eq(mod(x, 2), 0)
    >>> keep_ints(is_even, 5)
    2
    4
    """
##### Your code here #####

# done!