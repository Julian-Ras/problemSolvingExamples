"""
A Discrete Mathematics professor has a class of students. 
Frustrated with their lack of discipline, the professor decides
to cancel class if fewer than some number of students k are present 
when class starts.
"""

def angryProf(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    return ("YES" if count < k else "NO")

k = 3
a = [-1, -3, 4, 2]
res = angryProf(k, a)
print(res)