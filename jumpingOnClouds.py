"""
There is an array of clouds, c and an energy level e = 100. The character starts from c[0] 
and uses 1 unit of energy to make a jump of size k to cloud c[i + k]%n. If it lands on a 
thundercloud, c[i] = 1, its energy (e) decreases by 2 additional units. The game ends when 
the character lands back on cloud 0.
"""

def jumpingOnClouds(c, k):
    e = 100
    jumps = 0
    while(e > 0):
        jumps += k
        e -= 1
        if(jumps >= len(c)):
            jumps -= len(c)
        if(c[jumps] ==  1):
            e -= 2
        if(jumps == 0):
            return e
    return e


# c = [0,0,1,0]
# k = 2

# c = [0,0,1,0,0,1,1,0]
# k = 2

c = [1,1,1,0,1,1,0,0,0,0]
k = 3

print(jumpingOnClouds(c,k))