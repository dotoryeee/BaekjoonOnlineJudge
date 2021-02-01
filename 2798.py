import itertools
import sys

cards, target = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))
answer = []
for i in range(cards):
    temp = datas[i+1:]
    if len(temp) > 1:
        for j in itertools.combinations(temp, 2):
            tmp = sum(j) + datas[i]
            if tmp <= target:
                answer.append(tmp)
print(max(answer))