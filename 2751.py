import sys
count = int(sys.stdin.readline().rstrip())
li = []
for i in range(count):
    num = int(sys.stdin.readline().rstrip())
    li.append(num)
li.sort()
for i in li:
    print(i)