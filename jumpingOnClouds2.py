"""
There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. The player can 
jump on any cumulus cloud having a number that is equal to the number of 
the current cloud plus 1 or 2. The player must avoid the thunderheads. 
Determine the minimum number of jumps it will take to jump from the starting 
position to the last cloud. It is always possible to win the game.
"""

def jumpingOnClouds2(c):
    jumps = 0
    i = 0
    while i < len(c)-1:
        if (i+2)<=(len(c)-1) and c[i+2] == 0:
            i+=2
            jumps+=1
        else:
            i+=1
            jumps+=1
    return jumps
            
print(jumpingOnClouds2([0,1,0,0,0,1,0]))  
# print(jumpingOnClouds2([0,0,0,1,0,0])) 
# print(jumpingOnClouds2([0,1,0]))