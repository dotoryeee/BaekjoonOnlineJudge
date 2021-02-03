count = int(input())

for i in range(count):
    print(' '*int(count-i-1), end='')
    if i == count-1:
        print('*'*int(int(i*2)+1))
        break
    else:
        if i != 0:
            print('*', end='')
        print(' '*int(i*2-1),end='')
    print('*')