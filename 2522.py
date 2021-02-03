count = int(input())
for i in range(count):
    if i != 0:
        print(' '*int(count-i), end='')
        print('*'*i)
for i in range(count):
    print(' '*int(i),end='')
    print('*'*int(count-i))