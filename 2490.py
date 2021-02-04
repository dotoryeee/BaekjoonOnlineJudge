answer = []
for i in range(3):
    answer.append(sum(list(map(int, input().split()))))

for val in answer:
    if val == 1:
        print('C')
    elif val == 2:
        print('B')
    elif val == 3:
        print('A')
    elif val == 4:
        print('E')
    else:
        print('D')