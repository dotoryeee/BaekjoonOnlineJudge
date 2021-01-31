import sys
answer = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
word = sys.stdin.readline().rstrip()
cursor = 0
for char in word:
    if answer[ord(char)-97] == -1:
        answer[ord(char)-97] = cursor
    cursor += 1
for num in answer:
    print(num, end=' ')