import sys

corrected = [] #역순으로 수정된 숫자 목록

inputs = sys.stdin.readline().split()
for numbers in inputs:
    numbers = numbers[::-1]
    corrected.append(int(numbers))

if corrected[0] > corrected[1]:
    print(corrected[0])
else:
    print(corrected[1])