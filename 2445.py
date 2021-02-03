count = int(input())

for i in range(count):
    if i != 0:
        print('*'*i, end='')
        print(' '*int(int(count-i)*2), end='')
        print('*'*i)

for i in range(count, -1, -1):
    print('*'*i, end='')
    print(' '*int(int(count-i)*2), end='')
    print('*'*i)