import sys
data = sys.stdin.readline().rstrip()
count = 0
for i in data:
    print(i, end='')
    count += 1
    if count == 10:
        count = 0
        print()
