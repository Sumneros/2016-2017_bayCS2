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
    return raining or temp < 60


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

    if s1 > 29:
        if s2 > 29: print("No space left in either section")
        elif s2 == 29: print ("1 spot in Section 2.")
        else: print (str(30 - s2), "spots left in Section 2.")
    elif s2 > 29:
        if s1 == 30: print("1 spot in Section 1.")
        elif s1 < 29: print (str(30 - s1), "spots left in Section 1.")
    else: print("No overflow")

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
    for k in range(2, n):
        if mod(n, k) == 0: return False
    return n != 0 and n != 1
    
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
    for i in range(1, n + 1):
        fizz = mod(i, 3) == 0
        buzz = mod(i, 5) == 0
        if fizz and not buzz: print("fizz")
        elif buzz and not fizz: print("buzz")
        elif buzz and fizz: print("fizzbuzz")
        else: print(i)
        
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
    num, denom, i, j = 1, 1, 0, 0
    while le(i, sub(k, 1)):
        num = mul(num, sub(n, i))
        i = add(i, 1)
    while lt(j, k):
        denom = mul(denom, sub(k, j))
        j = add(j, 1)
    return floordiv(num, denom)
    
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
    i = 1
    while le(i, n):
        if cond(i): print(i)
        i = add(i, 1)
    
# done!