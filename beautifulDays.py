"""
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER i  the starting day number
  2. INTEGER j  the ending day number
  3. INTEGER k  the divisor

This function gets an initial day i  and a final day j
calculates (i - reverser(i))/k
for all numbers between i and j
if the result is an integer its a beautiful day
returns the count of beautiful days
"""



def beautifulDays(i, j, k):
    count = 0  
    for i in range(i,j + 1):
        condition = (i - int(str(i)[::-1])) % k == 0
        if condition:
            count += 1
    return count
            
            

res = beautifulDays(20, 23, 6)
print(res)
