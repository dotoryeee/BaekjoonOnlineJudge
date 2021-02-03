import sys
target = sys.stdin.readline().rstrip()
li = []
try:
    for i in range(int(target)-1, 0, -1):
        if i < int(target)-100:
            break
        sum = i
        for char in str(i):
            sum += int(char)
        if sum == (int(target)):
            li.append(i)
    print(min(li))
except:
    print(0)