"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. 
How tall will the tree be after  growth cycles?

For example, if the number of growth cycles is , the calculations are as follows:

Period  Height
0          1
1          2
2          3
3          6
4          7
5          14
"""

def utopianTree(n):
    """
    Using: (2**1) - 1 =  1,  (2**2) - 1 =  3, (2**3) - 1 =  7, (2**4) - 1 =  15,...
    and   (n/2) = number of even numbers below n without 0
    """
    if n == 0:
        height = 1
    elif n%2 == 0 and n > 0:
        exp = (n + 2)/2
        height = (2**(exp)) - 1
    else: 
        exp = (n + 3)/2
        height = (2**(exp)) - 2 
    return int(height)

res = utopianTree(6)
print(res)