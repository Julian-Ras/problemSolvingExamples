"""
The factorial of the integer n, written n!, is defined as:

n! = n x (n-1) x (n-2) x ... x 3 x 2 x 1

Calculate and print the factorial of a given integer.

For example, if n = 25, we calculate 25 x 24 x 23 x ... x 3 x 2 x 1
and get 15511210043330985984000000

"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
def fact_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod
    
# factorial of n recursion
print(fact(25))
# factorial of n iteration
print(fact_iter(25))