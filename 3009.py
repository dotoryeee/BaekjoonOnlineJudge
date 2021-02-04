import sys
xs, ys = [], []
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()
answer = []
if xs[0] == xs[1]:
    answer.append(xs[2])
else:
    answer.append(xs[0])
if ys[0] == ys[1]:
    answer.append(ys[2])
else:
    answer.append(ys[0])
for i in answer:
    print(i, end=' ')