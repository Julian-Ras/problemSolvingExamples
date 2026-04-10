"""
There is a list of 26 character heights (h) aligned by index to their letters. For example, 'a' is at index 0
and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area 
of the rectangle highlight in mm^2 assuming all letters are 1 mm wide.
"""

def highlightWordArea(h, word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    height = 0
    width = 0

    for i in word:
        for j in alphabet:
            if j == i:
                width += 1
                if height < h[alphabet.index(j)]:
                    height = h[alphabet.index(j)]
                break
    return height * width


# h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
# word = 'torn'

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,7]
word = 'zaba'

res = highlightWordArea(h, word)
print(res)