data = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        data.append(num)
if len(data) != 0:
    print(sum(data))
    print(min(data))
else:
    print(-1)