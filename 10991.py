count = int(input())

for i in range(count):
    print(' '*int(count-i-1), end='')
    for j in range(i+1):
        print('* ', end='')
    print()
