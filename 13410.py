target, count = map(int, input().split())
data = []
for i in range(count):
    num = str(int(i+1) * target)
    if len(num) != 1:
        num = num[::-1]
        data.append(int(num))
    else:
        data.append(int(num))
print(max(data))