from math import pow
li = [1, 1]
num = 0
while True: #리스트생성
    num += 1
    val = int(li[num-1]+pow(num, 2))
    if val >= 100001:
        break
    li.append(val)
print(li)

target = int(input())
for i, j in enumerate(li): #더 큰 값이 나오면 정지
    if target < j:
        print(i)
        break