import sys

tests = int(input())
datas = [] #테스트별 데이터
avgs = []
answer = []
avg_pointer = 0

for i in range(tests):
    line = list(map(int, sys.stdin.readline().split()))
    datas.append(line)

for i in datas:
    students = i[0]
    scores = i[1:]
    sum = 0
    for i in scores:
        sum += i
    avgs.append(sum/students)

    count = 0
    for score in scores:
        if avgs[avg_pointer] < score:
            count += 1
    answer.append(count/students)
    avg_pointer += 1

for i in answer:
    print(format(i*100, '.3f')+"%")
