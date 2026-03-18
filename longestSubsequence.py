"""
Given an array of integers, find the longest subsequence where 
the absolute difference between any two elements is less than 
or equal to 1
"""

def pickingNumbers(a):
    longest = 0
    # Check every element i with every element j in the array
    for i in a:
        countUp = 0
        countDown = 0
        for j in a:
        # To achieve absolute diff of 1, only 2 possible ways
        # (equal and Up) or (equal and Down)
            if j >= i and (j - i) <= 1:
                countUp += 1
            if j <= i and (i - j) <= 1:
                countDown += 1   
        # Compare counters
        if countUp == countDown and (countUp > longest):
            longest = countUp
        if countUp > countDown and (countUp > longest):
            longest = countUp
        if countDown > countUp and (countDown > longest):
            longest = countDown
    return longest
            
# a = [4, 6, 5, 3, 3, 1]  # solution: 3 --------> [4,3,3]
# a = [1, 2, 2, 3, 1, 2]  # solution: 5 --------> [1,2,2,1,2]
# a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  # solution: 20 --------> a
a = [
    14, 18, 17, 10, 9, 20, 4, 13, 19, 19, 8, 15, 15, 17, 6, 5, 15, 12, 18, 2, 
    18, 7, 20, 8, 2, 8, 11, 2, 16, 2, 12, 9, 3, 6, 9, 9, 13, 7, 4, 6, 
    19, 7, 2, 4, 3, 4, 14, 3, 4, 9, 17, 9, 4, 20, 10, 16, 12, 1, 16, 4, 
    15, 15, 9, 13, 6, 3, 8, 4, 7, 14, 16, 18, 20, 11, 20, 14, 20, 12, 15, 4, 
    5, 10, 10, 20, 11, 18, 5, 20, 13, 4, 18, 1, 14, 3, 20, 19, 14, 2, 5, 13
]  # solution 15: --------> several sequences of 15 (print counters to see)


res = pickingNumbers(a)
print(res)
