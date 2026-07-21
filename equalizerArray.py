"""
Given an array of integers, determine the minimum number of elements
to delete to leave only elements of equal value.

Example:

arr = [1,2,2,3]

Delete the 2 elements 1 and 3 leaving arr = [2,2]. If both 2s plus
either the 1 or the 3 are deleted, it takes 3 deletions to leave
either [1] or [3]. The minimum number of deletions is 2.
"""

def equalizeArray(arr):
    most_repeated = max(arr, key=arr.count)
    count = 0
    for item in arr:
        if item != most_repeated:
            count += 1
    return count

arr = [3, 3, 2, 1, 3]
# arr = [96, 96, 45, 52, 73, 44, 51, 96]

# arr = [24, 29, 70, 43, 12, 27, 29, 24,
#        41, 12, 41, 43, 24, 70, 24, 100,
#        41, 43, 43, 100, 29, 70, 100, 43,
#        41, 27, 70, 70, 59, 41, 24, 24, 29,
#        43, 24, 27, 70, 24, 27, 70, 24, 70,
#        27, 24, 43, 27, 100, 41, 12, 70, 43, 
#        70, 62, 12, 59, 29, 62, 41, 100, 43,
#        43, 59, 59, 70, 12, 27, 43, 43, 27,
#        27, 27, 24, 43, 43, 62, 43, 70, 29]

# arr = [10, 27, 9, 10, 100,
#        38, 30, 32, 45, 29,
#        27, 29, 32, 38, 32,
#        38, 14, 38, 29, 30,
#        63, 29, 63, 91, 54,
#        10, 63]

print(equalizeArray(arr))