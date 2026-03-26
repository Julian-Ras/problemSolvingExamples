"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

-The player with the highest score is ranked number  on the leaderboard.

-Players who have equal scores receive the same ranking number, and 
the next player(s) receive the immediately following ranking number.
"""

def climbingLeaderboard (ranked,player):
    unique_ranked = sorted(set(ranked), reverse=True) # ranked = [100,50,40,20,10]
    result = [] 
    n = len(unique_ranked) 
    i = n - 1 
    for score in player: 
        while i >= 0 and score >= unique_ranked[i]: 
            i -= 1                                               
        result.append(i + 2) 
        # i = 4, (score = 5) >= (unique_ranked = 10) ---> False, then result = [6]
        #--------------------------------------------------------------
        # i = 4, (score = 25) >= (unique_ranked = 10) ---> True, then result = [6]
        # i = 3, (score = 25) >= (unique_ranked = 20) ---> True, then result = [6] 
        # i = 2, (score = 25) >= (unique_ranked = 30) ---> False, then result = [6,4]
        #--------------------------------------------------------------
        # i = 2, (score = 50) >= (unique_ranked = 40) ---> True, then result = [6,4]
        # i = 1, (score = 50) >= (unique_ranked = 50) ---> True, then result = [6,4]
        # i = 0, (score = 50) >= (unique_ranked = 100) ---> False, then result = [6,4,2]
        #--------------------------------------------------------------
        # i = 0, (score = 120) >= (unique_ranked = 100) ---> True, then result = [6,4,2]
        # i = -1, while condition is False, then result = [6,4,2,1]
    return result

# Test 1
ranked = [100,100,50,40,40,20,10]
player = [5,25,50,120]

# # Test 2
# ranked = [100,90,90,80,75,60]
# player = [50,65,77,90,102]


r = climbingLeaderboard(ranked,player)
print(r)
