"""
Given a set of distinct integers, print the size of a maximal subset of S where 
the sum of any 2 numbers in S' is not evenly divisible by k. 

Example 
S = [19,10,12,10,24,25,22], k = 4. 
One of the arrays that can be created is S'[0] = [10,12,25]. Another is
S' = [19,22,24]. After testing all permutations, the maximum length solution 
array has 3 elements.
"""

def nonDivisibleSubset(k, s):
    # Count how many numbers have each remainder
    count = [0] * k
    
    for num in s:
        count[num % k] += 1
        
    result = 0

    # At most one number divisible by k
    if count[0] > 0:
        result += 1

    # Compare remainder pairs
    for r in range(1, (k + 1) // 2):
        result += max(count[r], count[k - r])

    # Handle the middle remainder when k is even
    if k % 2 == 0 and count[k // 2] > 0:
        result += 1

    return result



k = 7        
s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

# k = 3
# s = [1, 7, 2, 4]

# k = 4
# s = [19,10,12,10,24,25,22]


print(nonDivisibleSubset(k,s))