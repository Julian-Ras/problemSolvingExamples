"""
Given a sequence of n integers, p(1), p(2),...,   p(n) where each element is distinct and 
satisfies 1 <= p(x) <= n. For each x where 1 <= x <= n, that is x increments from 1 to n, 
find any integer y such that p(p(y)) == x and keep a history of the values of y in a return 
array.

Example:

p = [5,2,1,3,4]
p(1) = 5, p(2) = 2, p(3) = 1 ...

Each value of x between 1 and 5. the length of the sequence is analyzed as follows:
1. x = 1 == p(3), p(p(y)) = p(p(4)) = 3, so y = 4
2. x = 2 == p(2), p(p(y)) = p(p(2)) = 2, so y = 2
3. x = 3 == p(4), p(p(y)) = p(p(5)) = 4, so y = 5
4. x = 4 == p(5), p(p(y)) = p(p(1)) = 5, so y = 1
5. x = 5 == p(1), p(p(y)) = p(p(3)) = 1, so y = 3

the values for y are [4,2,5,1,3]
"""
def permutationEq(a):
    res = []
    for x in range(1,len(a) + 1):
        for val in a:
            if x == val:
                px = (a.index(val) + 1)
                for y in a:
                    if y == px:
                        res.append(a.index(y) + 1)
    return res



print(permutationEq([5,2,1,3,4]))