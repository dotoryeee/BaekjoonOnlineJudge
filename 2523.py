count = int(input())
for i in range(count):
    if i != 0:
        print('*'*i)
for i in range(count, -1, -1):
    print('*'*i)