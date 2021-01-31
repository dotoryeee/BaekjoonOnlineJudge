from sys import stdin
count = int(stdin.readline().rstrip())

for i in range(count):
    data = list(map(int, stdin.readline().split()))

for i in data:
    if i[0] > i[2]:
        print('10'+str(i[2]))
    else:
        floor = i[2] % i[0]
        num =