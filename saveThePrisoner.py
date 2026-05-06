"""
A jail has a number of prisoners and a number of treats to pass out to them. 
Their jailer decides the fairest way to divide the treats is to seat the prisoners 
around a circular table in sequentially numbered chairs. A chair number will be 
drawn from a hat. Beginning with the prisoner in that chair, one candy will be 
handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like 
all the others, but it tastes awful. Determine the chair number occupied by the 
prisoner who will receive that candy.

The function should return an integer representing the chair number of the 
prisoner to warn.

saveThePrisoner has the following parameter(s):

int n: the number of prisoners
int m: the number of sweets
int s: the chair number to begin passing out sweets from
"""

def saveThePrisoner(n, m, s):
    return (s + m - 2) % n + 1
            
               
print(saveThePrisoner(5,2,2))
print(saveThePrisoner(7,19,2))
print(saveThePrisoner(3,7,3))