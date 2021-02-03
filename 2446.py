count = int(input())

for i in range(count):
    print(' '*i, end='')
    print('*'*int(int(count-1-i)*2+1))

for i in range(count):
    if i != 0:
        print(' '*int(count-i-1), end='')
        print('*'*int(int(i*2)+1))