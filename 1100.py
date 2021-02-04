import sys
datas = []
count = 0
check_board = False
for _ in range(8):
    datas.append(sys.stdin.readline().rstrip())
for data in datas:
    check_board = not check_board
    for char in data:
        if check_board and char == 'F':
            count += 1
        check_board = not check_board
print(count)