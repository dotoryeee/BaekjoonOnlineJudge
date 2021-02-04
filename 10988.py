from math import ceil
word = input()
wo = word[:(int(len(word)/2))]
wo = wo[::-1]
if wo == word[int(ceil((len(word)/2))):]:
    print(1)
else:
    print(0)