count = int(input())
for i in range(count):
    print(' '*int(count-i-1), end='')
    print('*'*int(i*2+1))
for i in range(count-2, -1, -1):
    print(' '*int(count-i-1), end='')
    print('*'*int(i*2+1))