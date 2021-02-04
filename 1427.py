import sys
data = []
for num in sys.stdin.readline().rstrip():
    data.append(int(num))
data.sort(reverse=True)
for i in data:
    print(i, end='')