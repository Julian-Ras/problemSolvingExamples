"""
For each array, perform a number of right circular rotations and return
the values of the elements at the given indices.

circularArrayRotation has the following parameter(s):

list a:         input array
int k:          number of rotations
list queries:   indices of desired values

"""

def circularArrayRotation(a, k, queries):
    res = []
    k = k % len(a)  # ex: rot=2, len=5 -> k=2; rot=6, len=5 -> k=1
    arr = a[-k:] + a[:-k]
    for values in queries:
        res.append(arr[values])
    return res
   
print(circularArrayRotation([1,2,3,4,5], 2, [1,2,3]))