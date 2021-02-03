import sys
count = int(input())
datas = []
for i in range(count):
    datas.append(sys.stdin.readline().split())
for words in datas:
    for word in words:
        for char in word[::-1]:
            print(char, end='')
        print(' ', end='')
    print()