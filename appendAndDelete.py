"""

"""
def appendAndDelete(s, t, k):
    same = 0
    for i,j in zip(s,t):
        if i == j:
            same += 1
        else:
            break
    step = (len(s) - same) + (len(t) - same)
    if k >= len(s) + len(t):
        return "Yes"
    elif k < step:
        return "No"
    elif ((k - step) % 2 == 0):
        return "Yes"
    return "No"
    
# s = "aaaaaaaaaa"
# t = "aaaaa"
# k = 7

# s = "ashley"
# t = "ash"
# k = 2

# s = "aaa"
# t = "a"
# k = 5

# s = "y"
# t = "yu"
# k = 2

# s = "abcd"
# t = "abcdert"
# k = 10

# s = "zzzzz"
# t = "zzzzzzz"
# k = 4

s = "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
t = "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
k = 100


print(appendAndDelete(s, t, k))