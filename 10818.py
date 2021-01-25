import sys
count = int(input())
data = list(map(int, sys.stdin.readline().split()))
max = data[0]
min = data[0]
for i in data:
    if max < i:
        max = i
    if min > i:
        min = i
print(f'{min} {max}')