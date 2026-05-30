"""
An integer d is a divisor of an integer n if the remainder of (n / d) = 0.
Given an integer, for each digit that makes up the integer determine whether 
it is a divisor. Count the number of divisors occurring within the integer.

Examples:

n = 124

Check wether 1,2 and 4 are divisors of 124. All 3 numbers divide evenly into
124 so return 3.

n = 10

Check wether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.
"""

# Using str
def findDigitsStr(n):
    count = 0
    digits = [int(d) for d in str(n)] # 120 -> [1,2,0]
    for x in digits:
        if x == 0:
            continue
        elif n % x == 0:
            count += 1
    return count

def findDigitsStrMod10(n):
    num = n
    result = 0
    while num > 0:
        d = num%10
        num = int(num / 10)        
        if d == 0:
            continue
        if n % d == 0:
            result+=1
    return result

print(findDigitsStr(120))
print(findDigitsStrMod10(120))