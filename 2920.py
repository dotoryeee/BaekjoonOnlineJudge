import sys
data = list(map(int, sys.stdin.readline().split()))
if data[1]>data[0]:
    for num, i in enumerate(data[1:]):
        if data[num]>i:
            print('mixed')
            break
        elif num == len(data)-2:
            print('ascending')
else:
    for num, i in enumerate(data[1:]):
        if data[num]<i:
            print('mixed')
            break
        elif num == len(data)-2:
            print('descending')