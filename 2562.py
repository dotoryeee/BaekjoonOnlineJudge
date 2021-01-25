data = []
answer = [0, 0]
for i in range(9):
    num = int(input())
    data.append(num)
for num, value in enumerate(data):
    if value > answer[1]:
        answer = [num+1, value]
print(answer[1])
print(answer[0])