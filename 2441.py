count = int(input())

for i in range(count):
    print(' '*i, end='')
    print('*'*int(count-i))
