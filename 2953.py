import sys
data = []
for i in range(5):
    data.append(sum(list(map(int, sys.stdin.readline().split()))))
ans = 0
#print(data)
for num, val in enumerate(data):
    if val == max(data):
        ans = num+1
print(ans, data[ans-1])