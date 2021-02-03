count = int(input())

for i in range(count):
    if i == 0:
        print(' '*int(count-1), end='')
    else:
        print(' '*int(count-i-1), end='')
        print('*', end='')
    if i == 1:
        print(' ', end='')
    else:
        print(' '*int(int(i*2)-1),end='')
    print('*')
