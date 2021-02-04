target = int(input())
data = list(map(int, input().split()))
count = 0
for i in data:
    if i == target:
        count += 1
print(count)