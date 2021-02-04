import sys
datas = []

def checkNum(num):
    if num[0] % num[1] == 0:
        print('multiple')
    elif num[1] % num[0] == 0:
        print('factor')
    else:
        print('neither')


while True:
    data = (list(map(int, sys.stdin.readline().split())))
    if data == [0, 0]:
        break
    datas.append(data)

for i in datas:
    checkNum(i)