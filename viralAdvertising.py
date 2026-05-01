"""
When a company launch a new product, they advertise it to exactly 5 people
on social media. On the first day, half of those people (i.e floor(5/2))
likes the advertisement and each shares it to 3 of their friends.

Each day, (floor(recipients/2)) of the recipients like the advertisement and 
will share it with 3 friends on the following day. Assuming nobody receives 
the advertisement twice, determine how many people have liked the ad by the 
end of a given day, beginning with launch day as day 1.

Example:

n = 5

Day     Shared  Liked   Cumulative
1       5       2       2
2       6       3       5
3       9       4       9
4       12      6       15
5       18      9       24
"""

def viralAdvertising(n):
    shared = 5
    liked = 0
    res = 0
    for i in range(n):
        liked =  shared//2
        shared = liked * 3
        res += liked
        print(res)
    return res

viralAdvertising(5)