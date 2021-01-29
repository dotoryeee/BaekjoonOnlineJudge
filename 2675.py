import sys
datas = []
count = int(input())

for i in range(count):
    data = sys.stdin.readline().split()
    datas.append(data)

for data in datas:
    for i, char in enumerate(data):
        if i == 0:
            count = int(char) #반복개수(R) 가져오기
        else:
            for alphabet in char:
                print(alphabet * count, end='')
    print()