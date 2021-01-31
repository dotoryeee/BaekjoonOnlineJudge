import sys
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
word = sys.stdin.readline().rstrip()
for char in word:
    answer[ord(char)-97] += 1
for char in answer:
    print(char, end=' ')