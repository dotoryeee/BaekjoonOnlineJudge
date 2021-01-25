import sys
trash = input()
numbers = list(map(int, sys.stdin.readline().rstrip()))
sum = 0
for i in numbers:
    sum += i
print(sum)