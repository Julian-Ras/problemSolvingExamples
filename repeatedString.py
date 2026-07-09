"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first n letters of the 
infinite string.

Example:
s = "abcac"
n = 10

The substring we consider is "abcacabcac", the first 10 characters of the infinite string.
There are 4 occurrences of a in the substring.
"""

def repeatedString(s, n):
    count = 0
    count2 = 0
    for char in s:           # counting manually instead of s.count("a")
        if char == "a":
            count += 1
    subStr = (n//len(s))
    reminder = n%len(s)
    for char in s[:reminder]:
        if char == "a":
            count2 += 1
    total = count * subStr + count2
    return total

print(repeatedString("aba",10))
print(repeatedString("aab",882787))
print(repeatedString("a",1000000000000))