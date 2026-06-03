"""
Given the expected and actual return dates for a library book, create a program that calculates 
the fine (if any). The fee structure is as follows:

1- If the book is returned on or before the expected return date, no fine will be charged.

2- If the book is returned after the expected return day but still within the same calendar 
    month and year as the expected return date, 

    fine = 15*(number of days late)

3- If the book is returned after the expected return month but still within the same calendar
    year as the expected return date, 

    fine = 500*(number of months late)
4- If the book is returned after the calendar year in which it was expected, there is a fixed 
    fine of 10,000
"""

def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1 - y2) > 0:
        return 10000
    elif y1 < y2:
        return 0
    else:
        if ((m1 - m2) == 0) and (d1 > d2):
            return 15*(d1 - d2)
        elif (m1 - m2) > 0:
            return 500*(m1 - m2)
        else:
            return 0


# print(libraryFine(6,6,2015,9,6,2016))
print(libraryFine(2,7,1014,1,1,1015))
# print(libraryFine(2,7,1014,1,1,1014))